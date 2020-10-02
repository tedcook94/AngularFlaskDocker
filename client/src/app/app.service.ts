import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class AppService {
  constructor(private http: HttpClient) { }

  getHelloWorld () {
    return this.http.get<any>('/api/hw');
  };

  getUsers () {
    return this.http.get<any>('/api/users');
  };
}