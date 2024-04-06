import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { BrowseComponent } from '../../../pages/browse/browse.component';
import { AuthService } from '../../../shared/services/auth.service';
import { ProfileService } from '../../services/profile.service';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  constructor(private auth: AuthService, private profileService: ProfileService) { }
  profile: boolean = false;
  @Input({required: true}) header_email: string = '';
  @Input({required: true}) header_name: string = '';
  @Input({required: true}) header_picture: any = '';
  navlist = ['Home','TV Shows', 'Movies', 'New & Popular', 'Recently Added', 'My List', 'Browse by Languages'];

  signOut(){
    sessionStorage.removeItem("loggedInUser");
    this.auth.signOut();
  }

  toggleProfile(){
    if (!this.profile){
      this.profileService.openPopup();
    }
    else if (this.profile){
      this.profileService.closePopup();
    }
    this.profile = !this.profile
  }

}
