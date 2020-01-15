import { Component, OnInit, Type, Input } from '@angular/core';

@Component({
  selector: 'app-tableau',
  templateUrl: './tableau.component.html',
  styleUrls: ['./tableau.component.css']
})
export class TableauComponent implements OnInit {
  tableau: Array<{temp:number, hydro:number, lieu:string}>;
   
  
  constructor() {
    this.tableau= [ 
      {temp: 21, hydro: 50, lieu: 'cuisine'},
      {temp: 23, hydro: 49, lieu: 'chambre'},
      {temp: 22.5, hydro: 26, lieu: 'cave'} 
    ]; 
  }
  ngOnInit() {
  
  }
}
