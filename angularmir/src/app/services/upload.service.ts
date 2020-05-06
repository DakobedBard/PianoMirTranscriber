import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class UploadService {
  private documentsUrl = 'http://localhost:8000/upload';
  DJANGO_SERVER: string = "http://127.0.0.1:8000";
  constructor(private http: HttpClient) { }

  public uploadDocument(formData) {
    return this.http.post<any>(`${this.DJANGO_SERVER}/upload/create/`, formData);
  }
  getDocuments(id: any) {
    return this.http.get(this.documentsUrl+'/list/');
  }
  delete(id:any){
    return this.http.delete<any>(`${this.DJANGO_SERVER}/upload/${id}/delete/`);
  }

}
