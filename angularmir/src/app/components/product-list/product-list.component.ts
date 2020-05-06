import { Component, OnInit } from '@angular/core';
import {ProductService} from '../../services/product.service'
import { Product } from '../../models/product'
import { CartProduct } from '../../models/cart-product';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent implements OnInit {
  cart: CartProduct[] = [];
  products = [];
  // products = [
  //   {id: 1, imageurl:"https://dalinar-shoes.s3-us-west-2.amazonaws.com/air-jordan1-low.webp" , name: "airflow", "brand":'Nike', price:140},
  //   {id: 2, imageurl: "https://dalinar-shoes.s3-us-west-2.amazonaws.com/lebron17.webp" , name: "Lebron 17", "brand":'Nike', price:200},
  //   {id: 3, imageurl: "https://dalinar-shoes.s3-us-west-2.amazonaws.com/nike-kd13chill.webp", name: "KD Chill", "brand":'Nike', price:190},
  //   {id: 4, imageurl: "https://dalinar-shoes.s3-us-west-2.amazonaws.com/nike-squash.webp", name: "Nike Squash", "brand":'Nike', price:90},
  //   {id: 5, imageurl: "https://dalinar-shoes.s3-us-west-2.amazonaws.com/pegasus37.webp", name: "Pegasus 37", "brand":'Nike', price:140},
  // ];
  constructor(private productService :ProductService) {
  
   }

  ngOnInit() {
    this.getProducts();

  }

  getProducts():void{
    this.productService.getProducts().subscribe((data => {
      for (const d of (data as any)) {
        this.products.push({
          id: d.id,
          imageurl: d.imageurl,
          name: d.name,
          brand: d.brand,
          price: d.price
        });
      }
  }))
  }

}
