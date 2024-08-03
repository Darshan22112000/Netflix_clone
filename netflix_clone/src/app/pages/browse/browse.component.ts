import { Component, OnInit, inject, ChangeDetectorRef } from '@angular/core';
import { AuthService } from '../../shared/services/auth.service';
import { HeaderComponent } from "../../core/components/header/header.component";
import { CommonModule } from '@angular/common';
import { BannerComponent } from '../../core/components/banner/banner.component';
import { MovieService } from '../../shared/services/movie.service';
import { MovieCarouselComponent } from '../../shared/components/movie-carousel/movie-carousel.component';
import { IVideoContent } from '../../shared/models/video_content.interface';
import { forkJoin } from 'rxjs';
import { map } from 'rxjs/operators';

@Component({
    selector: 'app-browse',
    standalone: true,
    templateUrl: './browse.component.html',
    styleUrl: './browse.component.scss',
    imports: [CommonModule, HeaderComponent, BannerComponent, MovieCarouselComponent]
})
export class BrowseComponent implements OnInit{
  constructor(private auth: AuthService, private movieService: MovieService, private cd: ChangeDetectorRef) { }
  
  name = JSON.parse(sessionStorage.getItem("loggedInUser")!).name
  email = JSON.parse(sessionStorage.getItem("loggedInUser")!).email
  profile_picture = JSON.parse(sessionStorage.getItem("loggedInUser")!).picture // "./assets/img/netflix-profile-pictures.jpg"
  
  
  movies: IVideoContent[] = [];
  movieTitles: string[] = [];
  tvShowTitles: string[] = [];
  tvShows: IVideoContent[] = [];
  topRated: IVideoContent[] = [];
  nowPlaying: IVideoContent[] = [];
  ratedMovies: IVideoContent[] = [];
  upcomingMovies: IVideoContent[] = [];
  popularMovies: IVideoContent[] = [];

  // sources = [
  //   this.movieService.getMovies(),
  //   this.movieService.getTvShows(),
  //   this.movieService.getTopRated(),
  //   this.movieService.getNowPlayingMovies(),
  //   this.movieService.getRatedMovies(),
  //   this.movieService.getUpcomingMovies(),
  //   this.movieService.getPopularMovies()
  // ]

  ngOnInit(): void {
    this.movieService.getMovies().subscribe(res=>{
      this.movies = res.results;
      this.movieTitles = this.movies.map(movie => movie.title);
      this.cd.detectChanges();
    })

    this.movieService.getTvShows().subscribe(res=>{
      this.tvShows = res.results;
      this.tvShowTitles = this.tvShows.map(tvShow => tvShow.title);
      this.cd.detectChanges();
    })

    this.movieService.getTopRated().subscribe(res=>{
      this.topRated = res.results;
    })

    this.movieService.getNowPlayingMovies().subscribe(res=>{
      this.nowPlaying = res.results;
    })

    // this.movieService.getRatedMovies().subscribe(res=>{
    //   this.ratedMovies = res.results;
    // })

    this.movieService.getUpcomingMovies().subscribe(res=>{
      this.upcomingMovies = res.results;
    })

    this.movieService.getPopularMovies().subscribe(res=>{
      this.popularMovies = res.results;
    })


  }

  signOut(){
    sessionStorage.removeItem("loggedInUser");
    this.auth.signOut();
  }
}
  



