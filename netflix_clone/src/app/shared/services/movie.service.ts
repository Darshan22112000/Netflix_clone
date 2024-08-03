import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment'; // Import the 'environment' variable


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
