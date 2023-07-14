import { NgModule } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSidenavModule } from '@angular/material/sidenav';
import {MatCardModule} from '@angular/material/card';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { MenuComponent } from './menu/menu.component';

@NgModule({
  imports: [
    MatButtonModule,
    MatDialogModule,
    MatSidenavModule,
    MatCardModule,
],
  exports: [
    MatButtonModule,
    MatDialogModule,
    MatSidenavModule,
    MatCardModule,
],
  declarations: [
    HeaderComponent,
    FooterComponent,
    MenuComponent
  ]
})
export class MaterialModule { }

/*Exemplo de módulo contendo os componentes base do Angular Material*/
