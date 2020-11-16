import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { User } from '../models/user';

@Injectable()
export class AppService {
  constructor(private http: HttpClient) { }

  getHelloWorld () {
    return this.http.get<any>('/api/hw');
  };

  getUsers () {
    return this.http.get<User[]>('/api/users');
  };

  addUser (user: User) {
    return this.http.post<any>('api/users', user);
  }
  
  deleteUser (userId: number) {
    return this.http.delete<any>(`api/user/${userId}`);
  }
}