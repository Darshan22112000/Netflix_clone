import { Pipe, PipeTransform } from '@angular/core';
import e from 'express';

@Pipe({
  name: 'description',
  standalone: true
})
export class DescriptionPipe implements PipeTransform {

  transform(value: string, ...args: any): any {
    if (!value) {
      return '';
    }
    else if (value.length <= args) {
      return value;
    }else{
      return `${value.substring(0, args)}...`;
    }
  }

}
