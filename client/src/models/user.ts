import { EmailValidator } from "@angular/forms";

export class User {
  id: number;
  name: Name = new Name();
  email: string;
  password: string;
  active: boolean = true;
  created: Date;


}

class Name {
  first: string;
  last: string;
}