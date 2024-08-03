import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-movie-description',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './movie-description.component.html',
  styleUrl: './movie-description.component.scss'
})
export class MovieDescriptionComponent {
  @Input() movie: any;
}
