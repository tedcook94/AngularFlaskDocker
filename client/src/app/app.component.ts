import { Component, OnInit } from '@angular/core';

import { AppService } from './app.service';

import { User } from '../models/user';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  constructor(private service: AppService) {};

  ngOnInit() {
    this.service.getHelloWorld().subscribe(
      (hw: any) => {
        this.helloWorld = JSON.stringify(hw);
      }
    );
    this.service.getUsers().subscribe(
      (users: any) => {
        this.users = users.users.map((user: User) => {
          user.created = new Date(user.created);
          return user;
        });
      }
    );
  };

  addUser() {
    this.addError = '';
    this.service.addUser(this.newUser).subscribe(
      () => {
        this.newUser = new User();
        this.ngOnInit();
      },
      error => this.addError = error.message
    );
  }

  deleteUser(userId: number) {
    this.deleteError = '';
    this.service.deleteUser(userId).subscribe(
      () => this.ngOnInit(),
      error => this.deleteError = error.message
    );
  }
  
  title: String = 'Test Page';
  helloWorld: String = '';
  users: User[] = [];
  newUser: User = new User();
  addError: String = '';
  deleteError: String = '';
}
