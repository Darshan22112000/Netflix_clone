import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment'; // Import the 'environment' variable

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
  
  // public generateOrder = (params: object) => {
  //   const url = `${environment.serverUrl}/oms/generate-order`;
  //   return this.http.post(url, params);
  // }

  public getMovies = () => {
    const url = `${environment.serverUrl}/get_movies`;
    return this.http.get<any>(url);
  }

  public getTvShows = () => {
    const url = `${environment.serverUrl}/get_tv_shows`;
    return this.http.get<any>(url);
  }

  public getRatedMovies = () => {
    const url = `${environment.serverUrl}/get_rated_movies`;
    return this.http.get<any>(url);
  }

  public getNowPlayingMovies = () => {
    const url = `${environment.serverUrl}/get_now_playing_movies`;
    return this.http.get<any>(url);
  }

  public getPopularMovies = () => {
    const url = `${environment.serverUrl}/get_popular_movies`;
    return this.http.get<any>(url);
  }

  public getTopRated = () => {
    const url = `${environment.serverUrl}/get_top_rated_movies`;
    return this.http.get<any>(url);
  }

  public getUpcomingMovies = () => {
    const url = `${environment.serverUrl}/get_upcoming_movies`;
    return this.http.get<any>(url);
  }
}
