import { Component, OnInit } from '@angular/core';
import { CartProduct } from '../../../models/cart-product';
import { CartService } from '../../../services/cart.service';

@Component({
  selector: 'app-small-cart',
  templateUrl: './small-cart.component.html',
  styleUrls: ['./small-cart.component.scss']
})
export class SmallCartComponent implements OnInit {

  cart: CartProduct[] = [];
  constructor(private dataService: CartService) { }

  ngOnInit() {
    this.dataService.cart.subscribe(a => this.cart = a);
  }

  getCartProductItems(){
    this.cart = JSON.parse(localStorage.getItem('Cart'));
  }

  onRemoveProductsFromCart(productId: string){
    this.cart = this.cart.filter(a => a.productID != productId);
    localStorage.setItem('Cart', JSON.stringify(this.cart));
    this.dataService.updateCartItemCount(this.cart.length);
    this.dataService.updateShoppingCart(this.cart);
  }

}
