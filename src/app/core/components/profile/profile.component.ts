import { Component } from '@angular/core';
import { AuthService } from '../../../shared/services/auth.service';
import { ProfileService } from '../../services/profile.service';
import { HeaderComponent } from '../header/header.component';

@Component({
    selector: 'app-profile',
    standalone: true,
    templateUrl: './profile.component.html',
    styleUrl: './profile.component.scss',
    imports: [HeaderComponent]
})
export class ProfileComponent {
  constructor(private auth: AuthService, private profileService: ProfileService){}

  name = JSON.parse(sessionStorage.getItem("loggedInUser")!).name
  email = JSON.parse(sessionStorage.getItem("loggedInUser")!).email
  profile_picture = JSON.parse(sessionStorage.getItem("loggedInUser")!).picture // "./assets/img/netflix-profile-pictures.jpg"

  start = new Date(2024, 0, 1)
  end = new Date(2030, 0, 1)
  valid_date = new Date(this.start.getTime() + Math.random() * (this.end.getTime() - this.start.getTime()))
  valid_till = this.valid_date.getDate() + '-' + this.valid_date.getMonth() + '-' + this.valid_date.getFullYear()

  signOut(){
    this.profileService.closePopup();
    sessionStorage.removeItem("loggedInUser");
    this.auth.signOut();
  }
}
