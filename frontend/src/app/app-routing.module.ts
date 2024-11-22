import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { GuideComponent } from './components/pages/guide/guide.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent, title: 'PostDocs' },
  { path: 'guide', component: GuideComponent, title: 'PostDocs | Guide' },
  { path: '', redirectTo: 'home', pathMatch: 'full', title: 'PostDocs' }, /* Default Page */
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { onSameUrlNavigation: 'reload' })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
