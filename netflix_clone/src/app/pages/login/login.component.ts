declare var google: any;
import { CommonModule } from '@angular/common';
import { Component, Inject, OnInit } from '@angular/core';
import { Router, RouterModule } from '@angular/router';

@Component({
    selector: 'app-login',
    standalone: true,
    templateUrl: './login.component.html',
    styleUrl: './login.component.scss',
    imports: [CommonModule, RouterModule],
})
export class LoginComponent implements OnInit{
  // private router = Inject(Router) // does not inject Router, not redirecting to browse page on auth success
  
  constructor(private router: Router) { }
  ngOnInit(): void {
    google.accounts.id.initialize({
      client_id: '957118448943-3j4tmmucnhpsinovn7nb7u8icu7csq5k.apps.googleusercontent.com',
      callback: (resp: any)=>this.handleCredentialResponse(resp),
      // callback: this.handleCredentialResponse.bind(this),
      auto_select: false,
      cancel_on_tap_outside: true,
    });
    
    google.accounts.id.renderButton(
    document.getElementById("google-btn"),
      { 
        theme: "filled_blue", 
        size: "large", 
        shape:"rectangle", 
        width: "250" }
    );

    // @ts-ignore
    // google.accounts.id.prompt((notification: PromptMomentNotification) => {});
  }

  private decodeToken(token: string){
    return JSON.parse(atob(token.split(".")[1]))
  }
  
  handleCredentialResponse(response: any) {
    if (response){
      const payload = this.decodeToken(response.credential)
      sessionStorage.setItem("loggedInUser", JSON.stringify(payload))
      this.router.navigate(['/browse'])
    }
  }
   
}
