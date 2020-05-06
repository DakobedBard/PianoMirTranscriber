import { Component, OnInit } from '@angular/core';
import { CartService } from '../../services/cart.service';
import { Customer } from '../../models/customer';
import { Router } from '@angular/router';
import { CustomerService } from '../../services/customer.service';

@Component({
  selector: 'app-header',
  templateUrl: './app-header.component.html',
  styleUrls: ['./app-header.component.scss']
})
export class AppHeaderComponent implements OnInit {
   itemCount: number = 0;
  message: string;
  user: Customer;
  isLogged: boolean = false;
  constructor(private dataService: CartService,
              private customerService: CustomerService,
              private router: Router) { }

  ngOnInit() {
    this.dataService.count.subscribe(count => this.itemCount = count);
    if(localStorage.getItem('user') == 'undefined'){
      this.user = null;
    } else {
      this.user = JSON.parse(localStorage.getItem('user'));
    }
    this.isLogged = this.user != null;
  }

  // onLogout(){
  //   this.customerService.Logout().subscribe(a => {
  //     localStorage.removeItem('user');
  //     this.user = (localStorage.getItem('user') == 'undefined') ? null : JSON.parse(localStorage.getItem('user'));
  //     this.isLogged = this.user != null;
  //     window.location.reload();
  //   });
  // }

}
