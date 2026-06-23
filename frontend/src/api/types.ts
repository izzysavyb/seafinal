export interface AssetTypes {
  id?: number;
  name: string;
  category: string;
  serial_number: string;
  status: string;
  owner_id?: number;
}

export interface User {
  id: number;
  username: string;
  email: string;
  role: string;
}
