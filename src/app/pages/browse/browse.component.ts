import { Component, OnInit, inject } from '@angular/core';
import { AuthService } from '../../shared/services/auth.service';
import { HeaderComponent } from "../../core/components/header/header.component";
import { CommonModule } from '@angular/common';
import { BannerComponent } from '../../core/components/banner/banner.component';
import { MovieService } from '../../shared/services/movie.service';
import { MovieCarouselComponent } from '../../shared/components/movie-carousel/movie-carousel.component';

@Component({
    selector: 'app-browse',
    standalone: true,
    templateUrl: './browse.component.html',
    styleUrl: './browse.component.scss',
    imports: [CommonModule, HeaderComponent, BannerComponent, MovieCarouselComponent]
})
export class BrowseComponent implements OnInit{
  constructor(private auth: AuthService, private movieService: MovieService) { }
  
  name = JSON.parse(sessionStorage.getItem("loggedInUser")!).name
  email = JSON.parse(sessionStorage.getItem("loggedInUser")!).email
  profile_picture = JSON.parse(sessionStorage.getItem("loggedInUser")!).picture // "./assets/img/netflix-profile-pictures.jpg"
  
  ngOnInit(): void {
    this.movieService.getMovies().subscribe(res=>{
      console.log(res);
    })
  }

  signOut(){
    sessionStorage.removeItem("loggedInUser");
    this.auth.signOut();
  }
}
  



