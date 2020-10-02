import { Component } from '@angular/core';

import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  constructor(private service: AppService) { 
    this.service.getHelloWorld().subscribe(
      (hw: any) => {
        this.helloWorld = JSON.stringify(hw);
      }
    );
    this.service.getUsers().subscribe(
      (users: any) => {
        this.users = JSON.stringify(users);
      }
    );
  }
  
  title: String = 'Test Page';
  helloWorld: String = '';
  users: String = '';
}
