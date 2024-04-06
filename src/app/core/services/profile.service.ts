import { Injectable } from '@angular/core';
import { ProfileComponent } from '../components/profile/profile.component';
import { MatDialog } from '@angular/material/dialog';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  constructor(private dialog: MatDialog) {}

  openPopup() {
    this.dialog.open(ProfileComponent,{
      width: '100%',
      maxWidth: '75%',
      maxHeight: '500px',
      position: {left: '30%'} 
  });
  }
  closePopup(){
    this.dialog.closeAll()
  }
}
