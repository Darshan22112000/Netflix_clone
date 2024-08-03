// import { Injectable, inject } from '@angular/core';
// import { HttpClient } from '@angular/common/http';

// const options = {
//   headers: {
//     accept: 'application/json',
//     Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNjA2YThiZjRhZWNiNTU1NzMxNTc0NWJhMDcyMjg2MCIsInN1YiI6IjY2MDZjMWFhYTg5NGQ2MDE0OTYyMjQwMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zbI-l2Xoj2HzkbA5auCy_nKJJS80zFHrs4C6G0hVZrU'
//   },
//   params: {
//     include_adult: 'false',
//     include_video: 'true',
//     language: 'en-US',
//     page: '1',
//     sort_by: 'popularity.desc'
//   }
// };
// @Injectable({
//   providedIn: 'root'
// })

// export class MovieService {
//   constructor(public http: HttpClient) { }
  
//   getMovies(){
//       return this.http.get<any>('https://api.themoviedb.org/3/discover/movie', options)
//   }

//   getTvShows() {
//     return this.http.get<any>('https://api.themoviedb.org/3/discover/tv', options)
//   }

//   getRatedMovies() {
//     return this.http.get<any>('https://api.themoviedb.org/3/guest_session/guest_session_id/rated/movies', options)
//   }

//   getBannerImage(id: number) {
//     return this.http.get(`https://api.themoviedb.org/3/movie/${id}/images`, options)
//   }

//   getBannerVideo(id: number) {
//     return this.http.get(`https://api.themoviedb.org/3/movie/${id}/videos`, options);
//   }

//   getBannerDetail(id: number) {
//     return this.http.get(`https://api.themoviedb.org/3/movie/${id}`, options);
//   }

//   getNowPlayingMovies() {
//     return this.http.get<any>('https://api.themoviedb.org/3/movie/now_playing', options)
//   }

//   getPopularMovies() {
//     return this.http.get<any>('https://api.themoviedb.org/3/movie/popular', options)
//   }

//   getTopRated() {
//     return this.http.get<any>('https://api.themoviedb.org/3/movie/top_rated', options)
//   }

//   getUpcomingMovies() {
//     return this.http.get<any>('https://api.themoviedb.org/3/movie/upcoming', options)
//   }
// }
