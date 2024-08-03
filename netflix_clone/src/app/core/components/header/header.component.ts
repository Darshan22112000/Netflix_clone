import { CommonModule } from '@angular/common';
import { Component, Input, SimpleChanges } from '@angular/core';
import { BrowseComponent } from '../../../pages/browse/browse.component';
import { AuthService } from '../../../shared/services/auth.service';
import { ProfileService } from '../../services/profile.service';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { MatFormFieldModule } from '@angular/material/form-field'; 
import { MatAutocompleteModule } from '@angular/material/autocomplete'; 
import { ReactiveFormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, MatFormFieldModule, MatAutocompleteModule, ReactiveFormsModule, MatInputModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  constructor(private auth: AuthService, private profileService: ProfileService) { }
  profile: boolean = false;
  @Input() movieTitles: string[] = []; // Add this input
  @Input() tvShowsTitles: string[] = []; // Add this input
  @Input({required: true}) header_email: string = '';
  @Input({required: true}) header_name: string = '';
  @Input({required: true}) header_picture: any = '';
  navlist = ['Home','TV Shows', 'Movies', 'New & Popular', 'Recently Added', 'My List', 'Browse by Languages'];
  combinedList: string[] = [];
  
  searchControl = new FormControl();
  filteredMovies: Observable<string[]> | undefined;

  ngOnInit() {
    // this.filteredMovies = this.searchControl.valueChanges.pipe(
    //   startWith(''),
    //   map(value => this._filter(value))
    // );
    this.setupFilter();
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['movieTitles'] || changes['tvShowsTitles']) {
      this.setupFilter();
    }
  }

  setupFilter() {
    this.combinedList = this.movieTitles.concat(this.tvShowsTitles);
    this.filteredMovies = this.searchControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value))
    );
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    return this.combinedList.filter(movie => movie.toLowerCase().includes(filterValue));
  }

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

  onSearch() {
    const searchValue = this.searchControl.value;
    if (searchValue && this.combinedList.includes(searchValue)) {
      console.log(`Searching for movie: ${searchValue}`);
      // Implement the actual search functionality here
    } else {
      console.log('Movie not found');
    }
  }

}
