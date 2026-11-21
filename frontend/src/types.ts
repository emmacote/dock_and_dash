export interface Image {
    Id: string;
    Created: string;
    Os: string;
    Architecture: string;
    Comment: string;
}

export interface Volume {
    Name: string;
    CreatedAt: string;
    Mountpoint: string;
    Driver: string;
    Scope: string;
}

export interface Container {
  AppArmorProfile: string;
  Created: string;
  Driver: string;          
  HostnamePath: string;
  HostsPath: string;       
  Id: string;
  Image: string;        
  LogPath: string;
  MountLabel: string;   
  Name: string;
  Path: string;      
  Platform: string;
  ProcessLabel: string;
  ResolvConfPath: string;
}

export interface Network {
    Id: string;
    Name: string;
    Created: string;
    Driver: string;
    Scope: string;
}