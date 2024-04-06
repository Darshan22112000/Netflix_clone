import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const options = {
  headers: {
    accept: 'application/json',
    Authorization: ''
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
