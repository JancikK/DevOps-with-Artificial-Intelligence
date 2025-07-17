terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.33.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "DevOpsUA5_rg" {
  name     = "DevOpsUA5-resources"
  location = "West Europe"
}

# Network Security Group with Rules
resource "azurerm_network_security_group" "DevOpsUA5_nsg" {
  name                = "DevOpsUA5-nsg"
  location            = azurerm_resource_group.DevOpsUA5_rg.location
  resource_group_name = azurerm_resource_group.DevOpsUA5_rg.name

  security_rule {
    name                       = "AllowAllInboundTcp"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  tags = {
    environment = "Production"
  }
}

# Virtual Network
resource "azurerm_virtual_network" "DevOpsUA5_vnet" {
  name                = "DevOpsUA5-vnet"
  location            = azurerm_resource_group.DevOpsUA5_rg.location
  resource_group_name = azurerm_resource_group.DevOpsUA5_rg.name
  address_space       = ["10.0.0.0/16"]
  dns_servers         = ["10.0.0.4", "10.0.0.5"]

  tags = {
    environment = "Production"
  }
}

# Subnets
resource "azurerm_subnet" "DevOpsUA5_subnet1" {
  name                 = "subnet1"
  resource_group_name  = azurerm_resource_group.DevOpsUA5_rg.name
  virtual_network_name = azurerm_virtual_network.DevOpsUA5_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_subnet" "DevOpsUA5_subnet2" {
  name                 = "subnet2"
  resource_group_name  = azurerm_resource_group.DevOpsUA5_rg.name
  virtual_network_name = azurerm_virtual_network.DevOpsUA5_vnet.name
  address_prefixes     = ["10.0.2.0/24"]

  delegation {
    name = "nsg-delegation"
    service_delegation {
      name    = "Microsoft.Network/networkSecurityGroups"
      actions = ["Microsoft.Network/networkSecurityGroups/*"]
    }
  }

  # Associate NSG (use subnet association if required explicitly)
}

# Network Interface
resource "azurerm_network_interface" "DevOpsUA5_nic" {
  name                = "DevOpsUA5-nic"
  location            = azurerm_resource_group.DevOpsUA5_rg.location
  resource_group_name = azurerm_resource_group.DevOpsUA5_rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.DevOpsUA5_subnet1.id
    private_ip_address_allocation = "Dynamic"
  }
}

# Linux Virtual Machine
resource "azurerm_linux_virtual_machine" "DevOpsUA5_vm" {
  name                = "DevOpsUA5-machine"
  resource_group_name = azurerm_resource_group.DevOpsUA5_rg.name
  location            = azurerm_resource_group.DevOpsUA5_rg.location
  size                = "Standard_B1s"
  admin_username      = "adminuser"

  network_interface_ids = [
    azurerm_network_interface.DevOpsUA5_nic.id
  ]

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"  # Keep for lower cost
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  tags = {
    environment = "Development"
  }
}
