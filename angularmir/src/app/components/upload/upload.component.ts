import { Component, OnInit } from '@angular/core';
import { UploadService } from '../../services/upload.service';
import { FormBuilder, FormGroup } from '@angular/forms';
@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {
  form: FormGroup;
  DJANGO_SERVER = 'http://127.0.0.1:8000';
  imageURL;
  response;
  constructor(
    private uploadService: UploadService,
    private formBuilder: FormBuilder,) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      upload: [''],
      name: ['']
    });
  }
  onChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('upload').setValue(file);
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.form.get('upload').value);
    formData.append('name', this.form.get('name').value);
    formData.append('user', localStorage.getItem('currentUserID'));

    this.uploadService.uploadDocument(formData).subscribe(
      (res) => {
        this.response = res;
        this.imageURL = `${this.DJANGO_SERVER}${res.file}`;
      },
      (err) => {  
        console.log(err);
      }
    );
  }

}
