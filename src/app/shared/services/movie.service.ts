import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const options = {
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNjA2YThiZjRhZWNiNTU1NzMxNTc0NWJhMDcyMjg2MCIsInN1YiI6IjY2MDZjMWFhYTg5NGQ2MDE0OTYyMjQwMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zbI-l2Xoj2HzkbA5auCy_nKJJS80zFHrs4C6G0hVZrU'
  },
  params: {
    include_adult: 'false',
    include_video: 'true',
    language: 'en-US',
    page: '1',
    sort_by: 'popularity.desc'
  }
};
@Injectable({
  providedIn: 'root'
})

export class MovieService {
  constructor(public http: HttpClient) { }
  
  getMovies(){
      return this.http.get<any>('https://api.themoviedb.org/3/discover/movie', options)
  }
}
