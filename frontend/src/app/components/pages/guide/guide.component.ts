import { Component, AfterViewInit } from '@angular/core';
import { PrismService } from '../../../services/prism.service';
@Component({
  selector: 'app-guide',
  templateUrl: './guide.component.html',
  styleUrl: './guide.component.css',
  
})
export class GuideComponent {
  constructor( private prismService: PrismService ) {}

  ngAfterViewInit(): void {
    this.prismService.highlightAll();
  }
}
