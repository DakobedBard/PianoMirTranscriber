import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { ProductListComponent } from '../components/product-list/product-list.component'
import { UploadComponent } from '../components/upload/upload.component'
const routes: Routes = [{
  path: '',
  component: PagesComponent,
  children: [
    {
      path: '',
      redirectTo: 'products',
      pathMatch: 'full',
    },

    {
      path: 'upload',
      component: UploadComponent
    },

    {
      path: 'products',
      component: ProductListComponent,
    },
  ],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PagesRoutingModule {
}
