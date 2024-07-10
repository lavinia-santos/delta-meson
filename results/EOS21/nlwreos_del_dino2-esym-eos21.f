      PROGRAM nlrweos
      implicit double precision(a-h,o-z)
      LOGICAL CHECK
      logical sign,sign1
      REAL*8 xxx(2),FVEC(2),rmup,rmun,z(1),x(1)
      real*8 X0(1),X1(1),XMIN(1),XMAX(1),fout(1)
      real*8 X0a(1),X1a(1),XMINa(1),XMAXa(1)
      real*8 X0b(2),X1b(2),XMINb(2),XMAXb(2)
      real*8 xxx0(2),xxx1(2),xxxmin(2),xxxmax(2)
      REAL*8   RM, RMS, RMV, RMRho, gs, gv, grho, RKa, RLAMbda, xsi
      REAL*8   T,rhoinf,rhosup, a1, a2,pi,pi2,hc,drho,rho
      real*8 yp,dens,rhop,rhon,rnun
      real*8 rlambm,dmupdrhop,dmupdrhon,drndrp,rnrp,qui
      integer npoint,i,j,ipar
      common/temp/pi,pi2,gamma,rho0
      common/coup/rmv,rms,rmrho,gs,gv,grho,rka,rlambda,xsi
     1     ,gwr,gdel,rmdel,gr2,gdel2
      COMMON/PDN/X0,X1,XMIN,XMAX,stepmax,acc
      common/pdna/X0a,X1a,XMINa,XMAXa !,yp
      common/pdnb/X0b,X1b,XMINb,XMAXb !,yp
      common/fields/rphi,rv0,b0,rdel,rnun,rmun,ener
      COMMON/MA/RMe
      COMMON/ROS/RHOP,RHON,xkfp,xkfn
      common/vec/fvec
      common/esym/esy1
      external thermo,f3p,f3n,thermo1,y,yd,ya,yad,yx,yxd
      pi=dacos(-1.d0)
      pi2=pi*pi
      hc=197.326d0
      RM=939.D0
      gamma=2
c      gwr=0.d0
      rme=0.5d0
      gdel=0.d0
c$$$      write(6,*)'ipar,rho*(rm/hc)**3,rme,dener*rm
c$$$     1         ,xk*rm,q0a*rm,
c$$$     1         esy*rm,xl*rm,xksyma*rm,q0sym*rm,xkt*rm'
      Open(Unit=1,File='delta.inp')       
      Read(1,*)id,grho,gdel,gwr_gr2
       Close(1)
c     write(6,*)  grho,gdel,gwr
       gwr=gwr_gr2/grho**2
      ipar=0
c$$$      do i=25,30
c$$$         grho=i*1.d0
c$$$         do j=100,400
c$$$            gdel=j*.05d0
c$$$            do k=1,500
c$$$               gwr=k*0.00001
C-------------------------------------------------------
c     NLdelta 
C--------------------------------------------------------               
c      if(ipar.eq.16)then
c$$$         RM=939.D0
c$$$         RMS=550.D0/RM
c$$$         RMV=783.D0/RM
c$$$         RMRho=763.D0/RM
c$$$         RMDEL=980.d0/rm
c$$$         fs=10.33d0/(hc/rm)**2
c$$$         Gs=dsqrt(fs*rms**2)
c$$$         fv=5.42d0/(hc/rm)**2
c$$$         Gv=dsqrt(fv*rmv**2)
c$$$         fr=3.15d0/(hc/rm)**2
c$$$         Grho=2*dsqrt(fr*rmrho**2)
c$$$         fdel=2.5d0/(hc/rm)**2
c$$$         Gdel=dsqrt(fdel*rmdel**2)
c$$$         aa=0.033d0*hc/rm
c$$$         bb=-0.0048d0
c$$$         rka= 2*AA*gs**3    
c$$$         rlambda=6*BB*gs**4
c$$$         rb=aa
c$$$         rc=bb
c$$$         xsi=0.00
c$$$         gwr=0.0001d0        
c$$$         rho0=0.16d0/(rm/hc)**3
c         write(6,*)'gs,gv,grho,gdel,aa,bb,gwr='
c         write(6,*)gs,gv,grho,gdel,aa,bb,gwr
c         goto5
c      endif
c------------------------------------------
c     EOS21
c         EOS21 9.608190 11.957725 c11.087122c 3.117923 -4.098400
c                  0.000255 c0.040742c      
c------------------------------------------
c       if(ipar.eq.12)then
         rm=939.d0
         Rms=500.D0/RM
         RMV=782.50D0/RM
         RMRho=763.D0/RM
         RMDEL=980.d0/rm
         gs=9.608190d0
         gv=11.957725d0
c         grho=11.087122d0
         B=3.117923d0
         C=-4.098400d0
         XSI=0.000255d0
!         gwr=0.040742d0
         RKA=2*b*gs**3*1.d-3 
         RLAMBDA=6*c*gs**4*1.d-3
         rho0=0.155*(hc/rm)**3
c$$$c      endif
c$$$c------------------------------------------       
c$$$         grho=11.087122
c$$$         gdel=0.5346242543573545
c$$$         gwr=0.0032725986347310644

c$$$         grho=15.d0
c$$$         gdel=7.d0
c$$$         gwr=.001
c$$$C-------------------------------------------------------
c$$$  c     DINOa
c 490.050 93.9422 1115.15 154.436 805.891 4.9860 −0.01370 0.015 0.0016497         
c$$$C--------------------------------------------------------
c$$$      if(ipar.eq.17)then
c$$$         RM=939.D0
c$$$         RMS=490.05D0/RM
c$$$         RMV=782.5D0/RM
c$$$         RMRho=763.D0/RM
c$$$         RMDEL=980.d0/rm
c$$$         gsr2=805.891d0
c$$$         gdel2=1115.15d0/4.d0
c$$$         Gs=dsqrt(93.9422d0)
c$$$         Gv=dsqrt(154.436d0)
c$$$         Grho=dsqrt(805.891d0)
c$$$         Gdel=dsqrt(1115.15d0)*0.5d0
c$$$         aa=4.9860d0/rm
c$$$         bb=-0.01370d0
c$$$         rka= AA*gs**3    
c$$$         rlambda=BB*gs**4
c$$$         xsi=0.015d0
c$$$         gwr=0.0016497d0        
c$$$         rho0=0.1522d0/(rm/hc)**3
c         goto5
c$$$  endif
c$$$C-------------------------------------------------------
c$$$  c     DINOb
c          485.795 91.0316 1252.71 150.824 877.121 5.2914 −0.01488 0.015 0.0014014
        
c$$$C--------------------------------------------------------
c$$$      if(ipar.eq.17)then
c$$$         RM=939.D0
c$$$         RMS= 485.795/RM
c$$$         RMV=782.5D0/RM
c$$$         RMRho=763.D0/RM
c$$$         RMDEL=980.d0/rm
c$$$         Gs=dsqrt(91.0316d0)
c$$$         Gv=dsqrt(150.824d0)
c$$$         Grho=dsqrt(877.121d0)
c$$$         Gdel=dsqrt(1252.71d0)*0.5d0
c$$$         aa=5.2914d0/rm
c$$$         bb=-0.01488d0
c$$$         rka= AA*gs**3    
c$$$         rlambda=BB*gs**4
c$$$         xsi=0.015d0
c$$$         gwr=0.0014014d0        
c$$$         rho0=0.1525d0/(rm/hc)**3
c$$$c         goto5
c$$$  endif
c$$$C--------------------------------------------------------
c$$$      if(ipar.eq.17)then
c523.350 137.752 216.245 440.198 462.522 3.00645 −0.00735190 0.015 0.00285816 
C--------------------------------------------------------
c$$$         RM=939.D0
c$$$         RMS= 523.350/RM
c$$$         RMV=782.5D0/RM
c$$$         RMRho=763.D0/RM
c$$$         RMDEL=980.d0/rm
c$$$         Gs=dsqrt(137.752d0)
c$$$         Gv=dsqrt(216.245d0)
c$$$         Grho=dsqrt(440.198d0)
c$$$         Gdel=dsqrt(462.522d0)*0.5d0
c$$$         aa=3.00645d0/rm
c$$$         bb=-0.00735190d0
c$$$         rka= AA*gs**3    
c$$$         rlambda=BB*gs**4
c$$$         xsi=0.015d0
c$$$         gwr=0.00285816d0        
c$$$         rho0=0.152d0/(rm/hc)**3
c$$$c         goto5
c$$$  endif
c------------------------------------------
 5     continue
c         write(6,*)'gs,gv,grho,gdel,aa,bb,gwr='
c         write(6,*)gs,gv,grho,gdel,aa,bb,gwr
       stepmax=0.1D0
       x0(1)=rme
       x1(1)=rme*0.9d0
       acc=.1d-11  
       xmin(1)=0.D0
       XMAX(1)=1.D0
       acc=.1d-12 
       ierr=0
       xmina(1)=0.0D0
       XMAXa(1)=2.D0
c----------------
      stepmax=0.1D0
      x0b(1)=rme
      x0b(2)=rme*1.1
      x1b(1)=rme*0.9
      x1b(2)=rme*0.95
c     
      acc=.1d-12       
      ierr=0
      xminb(1)=0.d0
      xminb(2)=0.0D0
      xmaxb(1)=1.D0
      xmaxb(2)=1.D0
c---------------      
c$$$       write(6,*)'EoS,yp=?'
c$$$       read(5,*)yp
c$$$       write(6,*)'EoS, yp=',yp
c$$$c       write(6,*)'fort.60:ipar,rho0,EB,E_dens,pressure,
c$$$c     1     K0,Q0,Esym,L,Ksym, Qsym'

       yp=0.5
       do i=1,100
          rho=0.01*i*(hc/rm)**3
c          rho=rho0
          rhop=rho*yp
          rhon=rho-rhop
          rhob=rho
          rho3=rhop-rhon
          x0a(1)=rho*gv**2/rmv**2
          x1a(1)=x0a(1)*0.95
c----------------------------------------------------------
c    derivative calculation
c----------------------------------------------------------
c     
          yy=-rho3/rho
          call thermo(yy,rho,rme,esy,press,dener)
c          write(6,*)rho*(rm/hc)**3,dener*rm,rmun*rm,rme
!     &         ,rnun*rm,press*rm*(rm/hc)**3!
c          pause
          h=.002d0
          call thermo(yy,rho*(1.d0+h),rme,esy,press,dener)
          fm1p=esy
          gm1p=press
          dm1p=dener
c     
          call thermo(yy,rho*(1.d0-h),rme,esy,press,dener)
          fm1m=esy
          gm1m=press
          dm1m=dener
c     
          call thermo(yy,rho*(1.d0+2.d0*h),rme,esy,press,dener)
          gm2p=press
          fm2p=esy
          dm2p=dener
c     
          call thermo(yy,rho*(1.d0-2.d0*h),rme,esy,press,dener)
          fm2m=esy
          gm2m=press
          dm2m=dener

          call thermo(yy,rho,rme,esy,press,dener)
          fm0=esy
          gm0=press
          dm0=dener
          dener0=dener
          esy0=esy

          desymdr=(8.d0*(fm1p-fm1m)-fm2p+fm2m)/(12.d0*h*rho)
          denerdr=(8.d0*(dm1p-dm1m)-dm2p+dm2m)/(12.d0*h*rho)
          desymdr=(8.d0*(fm1p-fm1m)-fm2p+fm2m)/(12.d0*h*rho)
          dpressdr=(8.d0*(gm1p-gm1m)-gm2p+gm2m)/(12.d0*h*rho)
          d2enerdr2_5p=(-dm2p+16*dm1p-30.d0*dm0+16.d0*dm1m-dm2m)
     1         /(12.d0*h**2*rho**2)
          d2pressdr2_5p=(-gm2p+16*gm1p-30.d0*gm0+16.d0*gm1m-gm2m)
     1         /(12.d0*h**2*rho**2)

          d2pressdr2=(gm1p-2.d0*press+gm1m)/(h**2*rho**2)
          d2esymdr2=(fm1p-2.d0*esy+fm1m)/(h**2*rho**2)   
          d2esymdr2_5p=(-fm2p+16*fm1p-30.d0*fm0+16.d0*fm1m-fm2m)
     1         /(12.d0*h**2*rho**2)
          d3esymdr3= (fm2p-2.d0*fm1p+2.d0*fm1m-fm2m)/(2.d0*h**3*rho**3)   
          d3denerdr3=(dm2p-2.d0*dm1p+2.d0*dm1m-dm2m)/(2.d0*h**3*rho**3)   

          xK=9.d0*dpressdr-18*press/rho
          xKa=9.d0*rho0**2*d2enerdr2_5p
          q0a=27*rho0**3*d3denerdr3
          xl=3*rho0*desymdr
          xksym=9*d2esymdr2*rho0**2
          xksyma=9*d2esymdr2_5p*rho0**2
          q0sym=27*rho0**3*d3esymdr3
          xkt=xksym-6.*xl-q0/xk*xl
          xlv=3*rho*desymdr
          xksymav=9*d2esymdr2_5p*rho**2
c          if(esy*rm.gt.25.d0.and.xl*rm.gt.30.d0.and.esy*rm.lt.40.d0
c     1     .and.xl*rm.lt.140.d0)
c     1     ipar=ipar+1
c          if(esy*rm.gt.25.d0.and.xl*rm.gt.30.d0.and.esy*rm.lt.40.d0
c     1     .and.xl*rm.lt.140.d0)
           write(6,99)ipar,
     1        grho,gdel,gwr,rho*(rm/hc)**3,rme,dener*rm
     1         ,xk*rm,q0a*rm,
     1         esy*rm,xl*rm,xksyma*rm,q0sym*rm!,xkt*rm
           write(60,99)ipar,
     1        grho,gdel,gwr,rho,rho*(rm/hc)**3,rme,dener*rm
     1         ,xk*rm,q0a*rm,
     1         esy*rm,xl*rm,xksyma*rm,q0sym*rm,esy*rme!,xkt*rm

       enddo
c$$$      enddo
c        enddo
      
C-----------------------------------------------------------------
 99       format(2x,i5,2x,30(d10.4,1x))
 20    format(2x,10d13.4)
 32    format(2x,10d13.4)
       stop
       end      
c#######################################################################
c     SUBROTINAS
C#######################################################################
      subroutine thermo(yy,rho,rme,esy,press,dener)
      implicit none
      real*8 mup,mun,nup,nun,rho,v0,rhot,pi,rhoa,yy,yb,ybd
      real*8 delta,dens,press,rmup,rmun,rnup,rnun,T,ya,yda
      real*8 PI2,GS,GV,GRHO,RKA,RLAMBDA,XSI,RMA,RINFP,RINFN,RME
      real*8 RHOB,RHOP,RHON,RHO3,rhoin,del1,gr2,gdel2
      real*8 acc,stepmax,RPHI,B0,RV0,RM,RMS,RMV,RMRHO,gamma,y,yd
      real*8 X0(1),X1(1),XMIN(1),XMAX(1),x(1),rmdel,gdel
      real*8 X0a(1),X1a(1),XMINa(1),XMAXa(1),Za(1)
      real*8 X0b(2),X1b(2),XMINb(2),XMAXb(2),xb(2)
      real*8 ydb,xkfp,xkfn,gwr,dener,ener,esy,rmrho2,rho0
      real*8 yp,ef,xkf,res4n,res4p,res3n,res3p,f4p,f4n,f3p,f3n
      real*8 fd,fdel,rmep,rmen,rhos,rdel,esy1,esy2,esy3,esy00
      integer ierr,iact,ii,i      

      common/rhs/rhos
      common/ROS/RHOP,RHON,xkfp,xkfn
      common/temp/pi,pi2,gamma,rho0 
      common/coup/rmv,rms,rmrho,gs,gv,grho,rka,rlambda,xsi
     1     ,gwr,gdel,rmdel,gr2,gdel2
      COMMON/PDN/X0,X1,XMIN,XMAX,stepmax,acc
      common/pdna/X0a,X1a,XMINa,XMAXa
      common/pdnb/X0b,X1b,XMINb,XMAXb
      common/fields/rphi,rv0,b0,rdel,rnun,rmun,ener
      COMMON/MA/RMa
      common/esym/esy1
      external dnewto,y,yd,ya,yda,yb,ydb,f4p,f4n,f3p,f3n
c-----------------------------------------------------------------------
C     DADOS PARA DNEWTON
C-------------------------------------------------------
      yp=(1.d0-yy)/2.d0
      rhop=yp*rho
      rhon=rho-rhop
      ierr=0
      xkfp=(3.d0*pi2*rhop)**(1.d0/3.d0)
      xkfn=(3.d0*pi2*rhon)**(1.d0/3.d0)
      stepmax=0.1d0
      if(gdel.eq.0.d0)then
      call dnewto(x0,x1,xmin,xmax,1,y,yD,acc,
     1     stepmax,99,x,iact,ierr)
      RMEp=x(1)
      RMEn=x(1)
      rma=x(1)
      rme=rma
      rphi=(-RMa+1.D0)/GS
      rdel=0.d0
      else
      call dnewto(x0b,x1b,xminb,xmaxb,2,yb,ydb,acc,
     1     stepmax,109,xb,iact,ierr)
      RMEp=xb(1)
      RMEn=xb(2)
      rma=(rmep+rmen)/2.d0
      rme=rma
      rPHI=(-(rmep+rmen)+2.D0)/(2.d0*GS)
      rdel=(-rmep+rmen)/(2.d0*gdel)
      endif
c      write(6,*)'1',x(1),rho,yp,rphi,rdel,rmep,rmen
      NUP=dsqrt(xkfp**2+rmep**2)
      NUN=dsqrt(xkfn**2+rmen**2)
c      write(6,*)'2',yp,rhop,xkfn,nup,nun,rphi,rma
c      RPHI=(-RMe+1.D0)/GS
      RHOB=rhop+rhon
      RHO3=RHOP-RHON

      stepmax=0.05d0
      ierr=0
      call dnewto(x0a,x1a,xmina,xmaxa,1,ya,yDa,acc,
     1     stepmax,89,Za,iact,ierr)
c     write(6,*)'2',za(1)
c     pause
      rv0=za(1)/gv
      x1a(1)=za(1)
      x0a(1)=za(1)*0.98d0
      rmrho2=rmrho**2+2*gwr*grho**2*za(1)**2
      B0=GRHO/(2.D0*RMRHO2)*RHO3
c      write(6,*)'3',rv0,rmrho2,b0,za
C----------------------------------------------------------------
C     DEFININDO POTENCIAIS QUIMICOS
C------------------------------------------------------------------
      RMUP=NUP+GV*RV0+GRHO*B0/2.D0
      RMUN=NUN+GV*RV0-GRHO*B0/2.D0
c-------------------------------------------------------------------
C     DEFININDO ENERGIA, PRESSAO, ENTROPIA
C------------------------------------------------------------------
      rma=rmep
      CALL GAUSS(F3P,0.D0,xkfP,10,RES3P,II)
      rma=rmen
      CALL GAUSS(F3N,0.D0,xkfN,10,RES3N,II)
      ENER=GAMMA/(2.D0*PI2)*(RES3P+RES3N) 
     &     +GV*RV0*RHOB + GRHO/2.D0*B0*RHO3
     &     -RMV**2*RV0**2/2.D0 -XSI*GV**4*RV0**4/24.D0 
     &     -RMRHO**2*B0**2/2.D0
     &     +RMS**2*RPHI**2/2.D0 + RKA*(RPHI)**3/6.D0 
     &     + RLAMBDA*(RPHI)**4/24.D0
     &     -gwr*grho**2*gv**2*b0**2*rv0**2
     & +rmdel**2*rdel**2/2.D0
      DENER=ENER/RHOB-1.D0

c-------------------------------------------------------------------
C     DEFININDO PRESSAO
C------------------------------------------------------------------
      rma=rmep
      CALL GAUSS(F4P,0.D0,xKfP,10,RES4P,II)
      rma=rmen
      CALL GAUSS(F4N,0.D0,xKfN,10,RES4N,II)
      PRESS=GAMMA/(6.D0*PI2)*(RES4P+RES4N)+ RMV**2*RV0**2/2.D0
     &     +XSI*GV**4*RV0**4/24.D0 +RMRHO**2*B0**2/2.D0
     &     -RMS**2*RPHI**2/2.D0 - RKA*RPHI**3/6.D0 
     &     - RLAMBDA*RPHI**4/24.D0
     &     -rmdel**2*rdel**2/2.D0
     &     +gwr*grho**2*gv**2*b0**2*rv0**2
      rma=(rmep+rmen)/2.d0
      xkf=(3.d0*pi2*rhob/2.d0)**(1.d0/3.d0)
      ef=dsqrt(xkf**2+rma**2)
      if(gdel.ne.0.d0)fd=gdel**2/rmdel**2
      if(gdel.eq.0.d0)fd=0
      fdel=3.d0*(rhos/rma-rhob/ef)
      Esy=xkf**2/(6.d0*ef)+rhob/2.d0*(grho**2/rmrho2/4.d0
     1     -fd*(rma/ef)**2/(1.d0+fd*fdel))
      Esy1=xkf**2/(6.d0*ef)+rhob/2.d0*(grho**2/rmrho2/4.d0
     1     -fd*(rma/ef)**2/(1.d0+fd*fdel))
      
C      esy=xkf**2/(6.d0*ef)+rhob*grho**2*rmrho**2/rmrho2**2/8.d0-
c     1     0.5d0*fd*rma**2*rhob/(ef**2*(1+ fd*fdel))
c      write(6,*)'4',dener,rhos,rhob,xkf,press,xkf,ef,fd,fdel,esy
      return
      end
c-------------------------------------------------------
      function y(i,z,idim,ierr)
      IMPLICIT REAL*8 (A-H,O-Z)
      DIMENSION Z(1)
      external F1P,F1N
      COMMON/MA/RMA
      COMMON/ROS/RHOP,RHON,xkfp,xkfn
      common/temp/pi,pi2,gamma,rho0 
c      common/coup/rmv,rms,rmrho,gs,gv,grho,rka,rlambda,xsi,gwr
      common/coup/rmv,rms,rmrho,gs,gv,grho,rka,rlambda,xsi
     1     ,gwr,gdel,rmdel,gr2,gdel2
      common/rhs/rhos
      RMA=Z(1)
      PHI0=(-RMA+1.D0)/GS

      CALL GAUSS(F1P,0.D0,xkfp,10,RES1P,II)
      CALL GAUSS(F1N,0.D0,xkfn,10,RES1N,II)          
      RHOS=GAMMA/(2.D0*PI2)*RMA*(RES1P+RES1N)
      IF(I.EQ.1)Y=GS/(RMS**2)*RHOS-RKA/(2.D0*RMS**2)*
     &     PHI0**2-RLAMBDA/(6.D0*RMS**2)*(PHI0)**3 - PHI0    
c     write(6,*)'y',y,rma,rhos,rms,rka,res1p,res1n
      return
      end
c-----------------------------------------------------------------------------
      function yD(i,j,x,idim,ierr)
      IMPLICIT REAL*8 (A-H,O-Z)
      yd=0.D0   
      return
      end
c-------------------------------------------------------------------------
        function yb(i,z,idim,ierr)
        IMPLICIT REAL*8 (A-H,O-Z)
        DIMENSION Z(2)
        external F1P,F1N
        COMMON/ROS/RHOP,RHON,xkfp,xkfn
        common/temp/pi,pi2,gamma,rho0 
       common/coup/rmv,rms,rmrho,gs,gv,grho,rka,rlambda,xsi
     1     ,gwr,gdel,rmdel,gr2,gdel2
        COMMON/MA/RMA
        common/rhs/rhos
        RMAp=Z(1)
        RMAn=Z(2)
        xkfp=(3.d0*pi2*rhop)**(1.d0/3.d0)
        xkfn=(3.d0*pi2*rhon)**(1.d0/3.d0)
        PHI0=(-(rmap+rman)+2.D0)/(2.d0*GS)
        rdel=(-rmap+rman)/(2.d0*gdel)
        rma=rmap
        CALL GAUSS(F1P,0.D0,XKFP,10,RES1P,II)
        rma=rman
        CALL GAUSS(F1N,0.D0,xkFN,10,RES1N,II)
        RHOS=GAMMA/(2.D0*PI2)*(RMAP*RES1P+RMAN*RES1N)
        RHOS3=GAMMA/(2.D0*PI2)*(RMAP*RES1P-RMAN*RES1N)
        IF(I.EQ.1)Yb=GS/(RMS**2)*RHOS-RKA/(2.D0*RMS**2)*
     &       PHI0**2-RLAMBDA/(6.D0*RMS**2)*PHI0**3 - PHI0
        IF(I.EQ.2)Yb= Gdel/(RMdel**2)*RHOS3-rdel
c         write(6,*)yb,rms,rdel,rmdel
        return
        end
c-----------------------------------------------------------------------------
        function ydb(i,j,x,idim,ierr)
	IMPLICIT REAL*8 (A-H,O-Z)
        ydb=0.D0   
        return
        end
c-----------------------------------------------------------------------
      function ya(i,z,idim,ierr)
      IMPLICIT REAL*8 (A-H,O-Z)
      DIMENSION Z(1)
      external F1P,F1N
      COMMON/ROS/RHOP,RHON,xkfp,xkfn
      common/temp/pi,pi2,gamma,rho0 
      common/coup/rmv,rms,rmrho,gs,gv,grho,rka,rlambda,xsi
     1     ,gwr,gdel,rmdel,gr2,gdel2
c      common/coup/rmv,rms,rmrho,gs,gv,grho,rka,rlambda,xsi,gwr
      rv0=Z(1)/gv
      rho3=rhop-rhon
      rmrho2=rmrho**2+2*gwr*grho**2*z(1)**2
      B0=GRHO/(2.D0*RMRHO2)*rho3
      IF(I.EQ.1)ya=gv**2/rmv**2
     1     *(rhop+rhon-xsi/6.d0*(z(1))**3
     1     -2*gwr*z(1)*grho**2*b0**2)-z(1)   
c     write(6,*)'ya',ya,rv0*gv,rmrho2,gv
      return
      end
c-----------------------------------------------------------------------------
      function yda(i,j,x,idim,ierr)
      IMPLICIT REAL*8 (A-H,O-Z)
      ydA=0.D0   
      return
      end
c-------------------------------------------------------------------
      FUNCTION F1P(X)
      IMPLICIT REAL*8 (A-H,O-Z)
      COMMON/MA/RMA
      E=DSQRT(X*X+RMA*RMA)
      F1P=X*X/E
      RETURN
      END
C------------------------------------------------------------
      FUNCTION F1N(X)
      IMPLICIT REAL*8 (A-H,O-Z)
      COMMON/MA/RMA
      E=DSQRT(X*X+RMA*RMA)
      F1N=X*X/E
      RETURN
      END
C------------------------------------------------------------
      FUNCTION F2(X)
      IMPLICIT REAL*8 (A-H,O-Z)
      COMMON/MA/RMA
      E=DSQRT(X*X+RMA*RMA)
      F2=X*X
      RETURN
      END
C----------------------------------------------------------------
      FUNCTION F3P(X)
      IMPLICIT REAL*8 (A-H,O-Z)
      COMMON/MA/RMA
      RME=RMA
      E=DSQRT(X*X+RME*RME)
      F3P=X*X*E
      RETURN
      END
C-----------------------------------------------------------------
      FUNCTION F3N(X)
      IMPLICIT REAL*8 (A-H,O-Z)
      COMMON/MA/RMA
      RME=RMA
      E=DSQRT(X*X+RME*RME)
      F3N=X*X*E
      RETURN
      END
C------------------------------------------------------------------
      FUNCTION F4P(X)
      IMPLICIT REAL*8 (A-H,O-Z)
      COMMON/MA/RMA
      RME=RMA
      E=DSQRT(X*X+RME*RME)
      F4P=X**4/E
      RETURN
      END
c------------------------------------------------------------------
      FUNCTION F4N(X)
      IMPLICIT REAL*8 (A-H,O-Z)
      COMMON/MA/RMA
      RME=RMA
      E=DSQRT(X*X+RME*RME)
      F4N=X**4/E
      RETURN
      END
C---------------------------------------------------------------
      SUBROUTINE GAUSS(F,UG,OG,NN,FXINT,II)
      IMPLICIT DOUBLE PRECISION(A-H,O-Z)
      DIMENSION WG(10),ZG(10)
      DATA WG/0.6667134430869 D-01,
     C     0.1494513491506D00,
     C     0.2190863625160D00,
     C     0.2692667193100D00,
     C     0.2955242247148D00,
     C     0.2955242247148D00,
     C     0.2692667193100D00,
     C     0.2190863625160D00,
     C     0.1494513491506D00,
     C     0.6667134430869D-01/
      DATA ZG/-0.9739065285172D00,
     C     -0.8650633666890D00,
     C     -0.6794095682990D00,
     C     -0.4333953941292D00,
     C     -0.1488743389816D00,
     C     +0.1488743389816D00,
     C     +0.4333953941292D00,
     C     +0.6794095682990D00,
     C     +0.8650633666890D00,
     C     +0.9739065285172D00/

      FXINT=0.D0
      HH=(OG-UG)/DBLE(FLOAT(NN))
      U=UG
      O=U+HH
      KK=1
 24   OU=O+U
      RI=0.D0
      DO 26 I=1,10
         X=0.5D0*(ZG(I)*HH+OU)
         FUNCAO=F(X)
 26      RI=RI+WG(I)*FUNCAO
         FXINT=RI*HH/2.D0+FXINT
         KK=KK+1
         IF(KK-NN)28,28,9999
 28      U=O
         O=O+HH
         GO TO 24
 9999    RETURN
         END
c---------------------------------------------------------------
c---------------------------------------------------------------------------
c-----dnewto.for---911111 Coimbra 860117 Regensburg---Alex H.Blin-------------
      subroutine dnewto(x00,x11,xmin,xmax,idim,y,yp,acc,stemax,ilim,
     1                  x1,iact,ierr)
c-----Newton iteration procedure to find array x as zero of y(x)
c-----to an accuracy acc; real*8 version.
c-----if y' is a known function, set x0(*)=x1(*) and supply fct. yp;
c-----if y' is not known, supply some fct. yp (it will not be called).
c-----input:  x00(*),x11(*)= initial guesses for solution array, if
cx00=x11
c-----        then y' is calculated using function yp, otherwise
cnumerically;
c-----        xmin(*),xmax(*)= range in which search is to be confined,
cwith
c-----        restriction xmin<xmax;
c-----        idim = dimension of arrays x00,x11,xmin,xmax,x (max.
cidimx, see
c-----               data statement);
c-----        y,yp = external function names of y(x) and y'(x), to be
c-----               called as y(i,x,idim,ierr) (i= ith fct.y_i) and 
c-----               yp(i,j,x,idim,ierr) (j= partial derivative with
crespect 
c-----               to x(j)), sample fcts. at the end of this file;
c-----        acc = accuracy to which y(x)=0 to be found;
c-----        stemax = max. stepsize in searching x to avoid insta-
c-----                 bilities;
c-----        ilim = max. # of iterations.
c-----in/out: ierr= debug/error variable: in: < 0 displays debug data,
c-----        out: > 0 means error occurred.
c-----output: x1 = solution;
c-----        iact = actual number of iterations.
c-----note: this routine written for dimension of up to idimx (see
c-----data statement). To increase it, change idimx and arrays in
c-----dimension statement.
c-----note: This routine must be linked with function ddet for the 
c-----      calculation of the determinant of an idim*idim matrix.
c
      implicit real*8 (a-h)
      implicit real*8 (o-z)
c     external y,yp,ddet
      logical anal(6),ldeb
      dimension x00(idim),x11(idim),x1(idim),xmin(idim),xmax(idim),
     1     x0(6),xd(6),y1(6),d(6),xste(6),dydx(6,6),aa(6,6)
      data dz/1.d-100/,dinf/1.d30/,ideb/-0/,idimx/6/
c
      ldeb=ierr.lt.ideb
      if(idim.gt.idimx) goto 206
c     -300-
      do 300 j=1,idim
         if(xmin(j).ge.xmax(j)) goto 207
         anal(j)=x00(j).eq.x11(j)
         x0(j)=x00(j)
         x1(j)=x11(j)
         xste(j)=x1(j)-x0(j)
  300 continue
c     
c     -100-iteration loop
      do 100 i=1,ilim
         iact=i
         s=0.
c     -101-
         do 101 j=1,idim
            y1(j)=y(j,x1,idim,ierr)
            if(ierr.gt.0) goto 201
            s=s+y1(j)**2
 101     continue
         if(ldeb) write(*,*) ' dnewto #1: x1(*),y1(*),s=',x1,y1,s
         if(dsqrt(s).lt.acc) return
c     
c-----derivatives
c     -104-
         do 104 j=1,idim
c     -114-
            do 114 k=1,idim
c     
c-----analytic y'
               if(anal(j)) then
                  dydx(k,j)=yp(k,j,x1,idim,ierr)
                  if(ierr.gt.0) goto 202
                  if(ldeb) write(*,*) 
     1                 ' dnewto #2: k,j,dydx(k,j)=',k,j,dydx(k,j)
c     
c-----numerical y'
               else
c     -124-first store x1 in xd
                  do 124 l=1,idim
 124                 xd(l)=x1(l)
c-----now replace the j'th component by x0(j)
                     xd(j)=x0(j)
                     y0=y(k,xd,idim,ierr)
                     if(ierr.gt.0) goto 201
c-----new dydx only if xste>0, otherwise keep old value
              if(dabs(xste(j)).gt.dz) dydx(k,j)=(y1(k)-y0)/xste(j)
              if(ldeb) write(*,*) ' dnewto #3: k,j,x0(j),y0,dydx(k,j)=',
     1                    k,j,x0(j),y0,dydx(k,j)
                  endif
c     
                  a=dabs(dydx(k,j))
                  if(a.gt.dinf) goto 204
                  if(a.lt.dz) dydx(k,j)=dsign(dz,dydx(k,j))
                  if(a.eq.0.) dydx(k,j)=dz
 114           continue
 104        continue
c     
c-----idim*idim_determinants
            dn=ddet(dydx,idimx,idim,ierr)
            if(ierr.gt.0) goto 208
            if(dabs(dn).lt.dz) goto 205
c     -400-determinant in the numerator
            do 400 ii=1,idim
c     -410-first prepare matrix of dydx
               do 410 jj=1,idim
                  do 410 kk=1,idim
 410                 aa(jj,kk)=dydx(jj,kk)
c     -420-now overwrite the appropriate column with vector y1
                     do 420 jj=1,idim
 420                    aa(jj,ii)=-y1(jj)
                        d(ii)=ddet(aa,idimx,idim,ierr)
                        if(ierr.gt.0) goto 208
 400                 continue
c-----end of idim*idim_determinants
c     
                     s=0.
c     -103-
                     do 103 j=1,idim
                        x0(j)=x1(j)
                        xste(j)=d(j)/dn
              if(dabs(xste(j)).gt.stemax) xste(j)=dsign(stemax,xste(j))
                        x1(j)=x1(j)+xste(j)
                        if(x1(j).gt.xmax(j)) x1(j)=xmax(j)
                        if(x1(j).lt.xmin(j)) x1(j)=xmin(j)
                        s=s+xste(j)**2
 103                 continue
                     if(dsqrt(s).lt.dz) goto 203
 100              continue
c     
c-----errors
c     
 209  write(*,*) ' error 9 in dnewto: #_of_iterations too large, iact='
     1                 ,iact
         ierr=9
         return
c     
 208    write(*,*) ' error 8 in dnewto: error in ddet, ierr=',ierr
                  ierr=8
                  return
c     
 207    write(*,*) ' error 7 in dnewto: xmin not < xmax, xmin=',
     1                 xmin,' xmax=',xmax
                  ierr=7
                  return
c     
 206    write(*,*) ' error 6 in dnewto: dimension idim=',idim,
     1                 ' too large'
                  ierr=6
                  return
c     
 205    write(*,*) ' error 5 in dnewto: system of eqs. has no solution',
     1                 ' dn=',dn
                  ierr=5
      return
c     
 204  write(*,*) ' error 4 in dnewto: y'' too large, dydx(k,j)=',
     1     dydx(k,j)
      ierr=4
      return
c     
 203  write(*,*) ' error 3 in dnewto: accuracy cannot be reached, s=',s
      ierr=3
      return
c     
 202  write(*,*) ' error 2 in dnewto: error in yp, ierr=',ierr
      return
c     
 201  write(*,*) ' error 1 in dnewto: error in y, ierr=',ierr
      return
      end
c------------------------------------------------------------------------------
c-----program example----------------------------------------------------------
c     implicit real*8 (a-h)
c     implicit real*8 (o-z)
c     external y,yp
c     dimension x0(2),x1(2),x(2),xmin(2),xmax(2)
c     write(*,*) ' initial values x0(1),x0(2),x1(1),x1(2)?'
c     read (*,*) x0(1),x0(2),x1(1),x1(2)
c     write(*,*) ' accuracy?'
c     read(*,*) acc
c     ierr=0
c     xmin(1)=-100.
c     xmin(2)=-100.
c     xmax(1)= 100.
c     xmax(2)= 100.
c     call dnewto(x0,x1,xmin,xmax,2,y,yp,acc,10.,1000,x,iact,ierr)
c     write(*,*) 'x(1),x(2),iact',x(1),x(2),iact
c     stop
c     end
c------------------------------------------------------------------------------
c-----example for idim=2; solutions: x(1)=2., x(2)=-3.
c     function y(i,x,idim,ierr)
c     implicit real*8 (a-h)
c     implicit real*8 (o-z)
c     dimension x(idim)
c     if(i.eq.1) y=x(1)**4+x(2)**3+11.
c     if(i.eq.2) y=x(1)**2+x(2)-1.
c     return
c     end
c-----------------------------------------------------------------------------
c     function yp(i,j,x,idim,ierr)
c     implicit real*8 (a-h)
c     implicit real*8 (o-z)
c     dimension x(idim)
c     if(i.eq.1.and.j.eq.1) yp=4.*x(1)**3
c     if(i.eq.1.and.j.eq.2) yp=3.*x(2)**2
c     if(i.eq.2.and.j.eq.1) yp=2.*x(1)
c     if(i.eq.2.and.j.eq.2) yp=1.
c     return
c     end
c----------------------------------------------------------------------------
c-----ddet.for---911111 Coimbra 860504 Regensburg---Alex H.Blin---------------
      real*8 function ddet(a,idum,idim,ierr)
c-----calculates determinant of idim*idim_submatrix of idum*idum_array a,
c-----starting always with element a(1,1); real*8 version.
c-----input:  a(*,*)= idum*idum array representing the supermatrix
c-----        idum= dim. of array, max. see idumx in data statement;
c-----        idim= dim. of submatrix, max. idum.
c-----in/out: ierr= debug/error variable, in:<0 displays debug data,
c-----              out:>0 means error occurred.
c-----output: ddet= determinant of a(idim,idim) submatrix.
c-----note:   exchanging rows and columns doesn't matter.
      implicit real*8 (a-h)
      implicit real*8 (o-z)
      external ddet3,ddet4,ddet5,ddet6
      logical ldeb
      dimension a(idum,idum)
      data idumx/6/
c
      if(idum.gt.idumx) goto 101
      if(idim.gt.idum ) goto 102
      ldeb=ierr.lt.0
c     
      if(idim.eq.1) then
         ddet=a(1,1)
c     
      elseif(idim.eq.2) then
         ddet=a(1,1)*a(2,2)-a(1,2)*a(2,1)
c     
      elseif(idim.eq.3) then
         ddet=ddet3(a(1,1),a(1,2),a(1,3),
     1                    a(2,1),a(2,2),a(2,3),
     2                    a(3,1),a(3,2),a(3,3))
c     
      elseif(idim.eq.4) then
         ddet=ddet4(a(1,1),a(1,2),a(1,3),a(1,4),
     1                    a(2,1),a(2,2),a(2,3),a(2,4),
     2                    a(3,1),a(3,2),a(3,3),a(3,4),
     3                    a(4,1),a(4,2),a(4,3),a(4,4))
c     
      elseif(idim.eq.5) then
         ddet=ddet5(a(1,1),a(1,2),a(1,3),a(1,4),a(1,5),
     1                    a(2,1),a(2,2),a(2,3),a(2,4),a(2,5),
     2                    a(3,1),a(3,2),a(3,3),a(3,4),a(3,5),
     3                    a(4,1),a(4,2),a(4,3),a(4,4),a(4,5),
     4                    a(5,1),a(5,2),a(5,3),a(5,4),a(5,5))
      else
         ddet=ddet6(a(1,1),a(1,2),a(1,3),a(1,4),a(1,5),a(1,6),
     1                    a(2,1),a(2,2),a(2,3),a(2,4),a(2,5),a(2,6),
     2                    a(3,1),a(3,2),a(3,3),a(3,4),a(3,5),a(3,6),
     3                    a(4,1),a(4,2),a(4,3),a(4,4),a(4,5),a(4,6),
     4                    a(5,1),a(5,2),a(5,3),a(5,4),a(5,5),a(5,6),
     5                    a(6,1),a(6,2),a(6,3),a(6,4),a(6,5),a(6,6))
      endif
      if(ldeb) write(*,*) ' ddet: a(*,*)=',(i,(j,a(i,j),j=1,idim),
     1                    i=1,idim)
      return
c
c-----errors
  101 write(*,*) ' error in ddet: idum too large, idum=',idum
      ierr=1
      ddet=0.
      return
  102 write(*,*) ' error in ddet: idim too large, idim=',idim
      ierr=2
      ddet=0.
      return
      end
c------------------------------------------------------------------------------
c-----function ddet3 called by ddet--------------------------------------------
      real*8 function ddet3(a11,a12,a13,
     1                                a21,a22,a23,
     2                                a31,a32,a33)
c-----determinant of 3x3 matrix
      implicit real*8 (a-h)
      implicit real*8 (o-z)
      ddet3=a11*a22*a33+a12*a23*a31+a13*a21*a32
     1    -a31*a22*a13-a32*a23*a11-a33*a21*a12
      return
      end
c------------------------------------------------------------------------------
c-----function ddet4 called by ddet--------------------------------------------
      real*8 function ddet4(a11,a12,a13,a14,
     1                                a21,a22,a23,a24,
     2                                a31,a32,a33,a34,
     3                                a41,a42,a43,a44)
c-----determinant of 4x4 matrix
      implicit real*8 (a-h)
      implicit real*8 (o-z)
      external ddet3
      ddet4= a11*ddet3(a22,a23,a24,
     1                           a32,a33,a34,
     2                           a42,a43,a44)
      ddet4=-a12*ddet3(a21,a23,a24,
     1                            a31,a33,a34,
     2                            a41,a43,a44)+ddet4
      ddet4= a13*ddet3(a21,a22,a24,
     1                           a31,a32,a34,
     2                           a41,a42,a44)+ddet4
      ddet4=-a14*ddet3(a21,a22,a23,
     1                            a31,a32,a33,
     2                            a41,a42,a43)+ddet4
      return
      end
c-----function ddet5 called by ddet--------------------------------------------
      real*8 function ddet5(a11,a12,a13,a14,a15,
     1                                a21,a22,a23,a24,a25,
     2                                a31,a32,a33,a34,a35,
     3                                a41,a42,a43,a44,a45,
     4                                a51,a52,a53,a54,a55)
c-----determinant of 5x5 matrix
      implicit real*8 (a-h)
      implicit real*8 (o-z)
      external ddet4
      ddet5= a11*ddet4(a22,a23,a24,a25,
     1                           a32,a33,a34,a35,
     2                           a42,a43,a44,a45,
     3                           a52,a53,a54,a55)
      ddet5=-a12*ddet4(a21,a23,a24,a25,
     1                            a31,a33,a34,a35,
     2                            a41,a43,a44,a45,
     3                            a51,a53,a54,a55)+ddet5
      ddet5= a13*ddet4(a21,a22,a24,a25,
     1                           a31,a32,a34,a35,
     2                           a41,a42,a44,a45,
     3                           a51,a52,a54,a55)+ddet5
      ddet5=-a14*ddet4(a21,a22,a23,a25,
     1                            a31,a32,a33,a35,
     2                            a41,a42,a43,a45,
     3                            a51,a52,a53,a55)+ddet5
      ddet5= a15*ddet4(a21,a22,a23,a24,
     1                           a31,a32,a33,a34,
     2                           a41,a42,a43,a44,
     3                           a51,a52,a53,a54)+ddet5
      return
      end
c-----function ddet6 called by ddet--------------------------------------------
      real*8 function ddet6(a11,a12,a13,a14,a15,a16,
     1                                a21,a22,a23,a24,a25,a26,
     2                                a31,a32,a33,a34,a35,a36,
     3                                a41,a42,a43,a44,a45,a46,
     4                                a51,a52,a53,a54,a55,a56,
     5                                a61,a62,a63,a64,a65,a66)
c-----determinant of 6x6 matrix
      implicit real*8 (a-h)
      implicit real*8 (o-z)
      external ddet5
      ddet6= a11*ddet5(a22,a23,a24,a25,a26,
     1                           a32,a33,a34,a35,a36,
     2                           a42,a43,a44,a45,a46,
     3                           a52,a53,a54,a55,a56,
     4                           a62,a63,a64,a65,a66)
      ddet6=-a12*ddet5(a21,a23,a24,a25,a26,
     1                            a31,a33,a34,a35,a36,
     2                            a41,a43,a44,a45,a46,
     3                            a51,a53,a54,a55,a56,
     4                            a61,a63,a64,a65,a66)+ddet6
      ddet6= a13*ddet5(a21,a22,a24,a25,a26,
     1                           a31,a32,a34,a35,a36,
     2                           a41,a42,a44,a45,a46,
     3                           a51,a52,a54,a55,a56,
     4                           a61,a62,a64,a65,a66)+ddet6
      ddet6=-a14*ddet5(a21,a22,a23,a25,a26,
     1                            a31,a32,a33,a35,a36,
     2                            a41,a42,a43,a45,a46,
     3                            a51,a52,a53,a55,a56,
     4                            a61,a62,a63,a65,a66)+ddet6
      ddet6= a15*ddet5(a21,a22,a23,a24,a26,
     1                           a31,a32,a33,a34,a36,
     2                           a41,a42,a43,a44,a46,
     3                           a51,a52,a53,a54,a56,
     4                           a61,a62,a63,a64,a66)+ddet6
      ddet6=-a16*ddet5(a21,a22,a23,a24,a25,
     1                            a31,a32,a33,a34,a35,
     2                            a41,a42,a43,a44,a45,
     3                            a51,a52,a53,a54,a55,
     4                            a61,a62,a63,a64,a65)+ddet6
      return
      end
c------------------------------------------------------------------------------
c-----program example
c     dimension a(4,4)
c     ierr=0
c     k=0
c     do 100 i=1,4
c     do 100 j=1,4
c     k=k+1
c 100 a(i,j)=k
c     a(1,1)=-1.
c     a(4,4)=-16.
c     do 110 i=1,4
c     d=ddet(a,4,i,ierr)
c 110 write(*,*) d
c     write(*,*) ' -1., -16., 8., -256.'
c     stop
c     end

      
c      include 'dnewton.f'
c     include 'broydn.f'



