import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Product } from '../models/product'
import { catchError, map, tap } from 'rxjs/operators';



@Injectable({
  providedIn: 'root'
})
export class ProductService {


  private productsURL = 'http://localhost:8040/products';
  constructor(private http: HttpClient){}
  
  getProducts(): Observable<Product[]>{
    return this.http.get<Product[]>(this.productsURL)
  }
  
  getProductID(){
    
  }

  getProductDetailsById(id: string): Observable<Product> {
    console.log("The id of the route is " + id)
    var route = `${this.productsURL}/idx?id=${id}`
    console.log("The route is " + route)
    const url = `${this.productsURL}/idx?id=${id}`;
    return this.http.get<Product>(url).pipe(
      catchError(this.handleError<Product>(`getProduct id=${id}`))
    );
  }
  
    /** GET hero by id. Will 404 if id not found */
  getProduct(id: string): Observable<Product> {
  
    const url = `${this.productsURL}/idx?id=${id}`;
    return this.http.get<Product>(url).pipe( 
      catchError(this.handleError<Product>(`getProduct id=${id}`))
    );
  }
  
  
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
