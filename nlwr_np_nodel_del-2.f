      program nlwr_np_nodel_del
C     CALCULATES THE EOS FOR THE BARYON OCTET MODEL (NLWM) AT T=0
C
      IMPLICIT DOUBLE PRECISION(A-H,O-Z)
      LOGICAL check
      DIMENSION X(7),FVEC(7), XH(3),SB(8), GSS(8), Gphi(8),Uh(8),rmef(8)
      DIMENSION RMB(8),RML(2),QB(8),RI3(8),GS(8),GV(8),GR(8),ri3d(8)
      DIMENSION RNB(8),RNL(2),rmuba(8),rnbc(7),uhb(8),rmlandau(8)
      real*8 gdel(8),gdeln
      integer*4 lll(7)
      real*8 xxx(7)
      real*8 ronset(8,6)
      COMMON/CDATA/RMB,RML,RMS,RMV,RMR,RMSS,RMphi,rmdel,RB,RC,RXI,rlv,
     &             GS,GV,GR,GSS,Gphi,QB,RI3,GDEL,RI3D,gdeln
      COMMON/CNBT/RNBT,RNL,SB,SCHARGEB
      COMMON/CFVEC/FVEC
      COMMON/CDATAQ/PI2,g,hbc,rm,ipar
      common/lep/enerlep,presslep,ener,press,rnb,rmuba,dpressf,denerf
      common/rmu/rmef,rmule,rmlandau
c---------------------------------------------------------------------
      DATA RMB/939.565d0,938.272d0,1115.63d0,1193.12d0,1193.12d0
     &,1193.12d0,1318.1d0,1318.1d0/
      DATA RML/0.511d0,105.66d0/
      DATA QB/0.0d0,1.0d0,0.0d0,1.0d0,0.0d0,-1.0d0,0.0d0,-1.0d0/
      DATA SB/0.0d0,0.0d0,-1.d0,-1.d0,-1.d0,-1.d0,-2.d0,-2.d0/
      DATA RI3/-0.5d0,0.5d0,0.0d0,1.0d0,0.0d0,-1.0d0,0.5d0,-0.5d0/
      DATA RI3D/-1.d0,1.d0,0.0d0,-2.0d0,0.0d0,2.0d0,-1.d0,1.d0/
C---------------------------------------------------------------------
C     1=neutron,2=proton,3=lambda,4=sigma+,5=sigma0,6=sigma-,7=cascade0,8=cascade-
C     1=electron,2=muon
c---------------------------------------------------------------------
      PI =DACOS(-1.D0)
      PI2=PI*PI
      HBC=197.326d0
      rm=939.d0
      RMDEL=980.d0/rm
      rhoc=1.5d0*(hbc/rm)**3
      Open(Unit=1,File='delta.inp')
      write(6,*)'ipar,gr,gdel,lambda_v'
      read(1,*)ipar,grn,gdeln,rlv_gr2
      Close(1)
      write(6,*)ipar,grn,gdeln,rlv_gr2
      rlv=rlv_gr2/grn**2
      ass=1.d-6
      npoint=501
      RMDEL=980.d0/RM
c------------------------------------------
c     EOS18
c         EOS18 9.220247 11.170082 11.087122 4.036904 -4.553914 0.003810 0.040742      
c------------------------------------------
         rm=939.d0
         Rms=500.D0/RM
         RMV=782.50D0/RM
         RMR=763.D0/RM
         RMDEL=980.d0/rm
         gsn=9.220247d0
         gvn=11.170082d0
c         grn=11.087122d0
         B=4.036904d-3
         C=-4.553914d-3
         rxi=0.003810d0
         rc=c
         rb=b
!         rlv=0.040742d0
!         gdeln=0.d0
c         RKA=2*b*gsn**3 
c         RLAMBDA=6*c*gsn**4
         rho0=0.155d0*(hbc/rm)**3
         denss=0.155d0

c$$$C-------------------------------------------------------
c$$$c     NLdelta 
c$$$C--------------------------------------------------------
c$$$      if(ipar.eq.13)then
c$$$         RM=939.D0
c$$$         RMS=550.D0/RM
c$$$         RMV=783.D0/RM
c$$$         RMR=763.D0/RM
c$$$         RMDEL=980.d0/rm
c$$$         RMSS=975.0d0/RM
c$$$         RMphi=1020.0d0/RM
c$$$         GSS(1)=0.0d0
c$$$         Gphi(1)=0.0d0
c$$$         fs=10.33d0/(hbc/rm)**2
c$$$         Gsn=dsqrt(fs*rms**2)
c$$$         fv=5.42d0/(hbc/rm)**2
c$$$         Gvn=dsqrt(fv*rmv**2)
c$$$         fr=3.15d0/(hbc/rm)**2
c$$$         Grn=2*dsqrt(fr*rmr**2)
c$$$         fdel=2.5d0/(hbc/rm)**2
c$$$         Gdeln=dsqrt(fdel*rmdel**2)
c$$$         aa=0.033d0*hbc/rm
c$$$         bb=-0.0048d0
c$$$         rka= 2*AA*gsn**3    
c$$$         rlambda=6*BB*gsn**4
c$$$         rb=aa
c$$$         rc=bb
c$$$c         RB=rka/2.d0
c$$$c         RC=rlambda/6.d0
c$$$         rxi=0.00
c$$$         rlv=0.d0
c$$$         
c$$$         rho0=0.148d0/(rm/hbc)**3
         S=382.22864024231552d0/rm
         V=309.22267476897025d0/rm
         rsl=0.619d0
         rssl=0.553d0
         rpl=-dsqrt(2.d0)/3.d0
         rwl=2.d0/3.d0
         rsx_1p=0.311d0
c$$$      endif
C--------------------------------------------------------------------- 
      DO I=3,8
         RMB(I)=RMB(I)/rm
      ENDDO
      DO I=1,2
         RMB(I)=RMB(I)/RM
         RML(I)=RML(I)/RM
      ENDDO
       zz=1.d0/dsqrt(6.d0)
       xn=0.d0
c---------------------------------------------------------------------
      DO I=1,2
         GS(I)=GSN
         GV(I)=GVN
         GR(I)=GRN
         gdel(i)=gdeln
         GSS(i)=0.0d0 !sigmas-hiperon coupling constant       
         Gphi(i)=0.d0 ! phi-hiperon coupling constant                  
      ENDDO
      ph=0.d0     
c---------------------------------------------------------------------
c--------------------------------------------------------------------- 
      DO i=3,3
         gv(i)=rwl*gv(1)
         GR(i)=GR(1)*0.0d0           !rho-hiperon coupling constant 
         gphi(i)=rpl*gv(1)
         gs(i)=rsl*gs(1)
         gdel(i)=0.d0
         gss(i)=rssl*gs(1)
!        UHb(i)=GV(i)/GV(1)*V-GS(i)/GS(1)*S
         UHb(i)=V-S
c         write(6,*)uhb(i)*rm
c         pause
      ENDDO
      DO i=7,8       
         GV(i)=gv(1)*rwl*0.5d0   
         GR(i)=GR(1)    !rho-hiperon coupling constant
         gdel(i)=gdel(1)
         Gphi(i)=rpl*2.d0*GV(1)
         GS(i)=rsx_1p*gs(1) !sigma-hiperon coupling constant
         GSS(i)=1.d-8*GS(1)     !*dsqrt(2.0d0)/3.0d0 sigmas-hiperon coupling c
      ENDDO
c---------------------------------------------------------------------
C     Initializing variables
C---------------------------------------------------------------------
      RNBINF=0.05d0
      RNBSUP=1.d0 !
      NPOINT=501
      RNBINF=RNBINF/(RM/HBC)**3
      RNBSUP=RNBSUP/(RM/HBC)**3
      DNB=(RNBSUP-RNBINF)/(NPOINT-1)   
c---------------------------------------------------------------------
      do iii=3,3
         usig=(-10.d0+(iii-1)*20.d0)
      uh(4)=usig/rm!
      uh(5)=uh(4)
      uh(6)=uh(4)
c      write(7,*)'ipar,Usig,Npoints=',ipar,Usig,npoint
      DO i=4,6
         GV(i)=GV(1)*rwl  !omega-hiperon coupling constant        
         GR(i)=GR(1)             !rho-hiperon coupling constant
         gdel(i)=gdel(1)
         Gphi(i)=rpl*GV(1)      ! phi-hiperon coupling
         GS(i)=(GV(i)/GV(1)*V-UH(i))/S*GS(1) !sigma-hiperon coupling
         GSS(i)=0.1d-8!5.482d0*ass   !dsqrt(2.0d0)/3.0d0!sigmas-hiperon 
      ENDDO
      write(6,*)gs(4)/gs(1)
      do i=1,8
         rnb(i)=0.d0
      enddo   

      do i=1,7
         x(i)=0.d0
         fvec(i)=0.d0
      enddo
      rmun=0.d0
      vomega=0.d0
      vsigma=0.d0
      vsigmas=0.d0
      rmue=0.d0
      vphi=0.d0
      vrho=0.d0
      X(1)=1.0024722139031694        
      X(2)=2.2493037831483487E-002  
      X(3)=0.20109550264731024       
      X(4)=0.16609149192941339       
      X(5)=-1.0989909721155176E-002   
      X(7)=2.0246847119907045E-007   
c      X(6)=1.000000000000000e-7      
      X(6)=0.001d0      
c     X(8)=1.1444732308518724E-006
      
      do i=1,7
         lll(i)=0
         rnbc(i)=0
      enddo
      
C---------------------------------------------------------------------
C     Main loop
C---------------------------------------------------------------------
      enerold=0.D0
      pressold=0.d0
      DO i=1,npoint
            do j=1,8
         rnb(j)=0.d0
      enddo   
         rnbt=rnbinf+(i-1)*dnb
c$$$         if(rnbc(1).eq.rhoc.and.rnbc(4).eq.rhoc.and.rnbc(6).eq.rhoc)then
c$$$            X(6)=1.0246847119907045E-01   
c$$$            X(7)=1.000000000000000e-7     
c$$$         endif
c         if(ipar.le.12)CALL newt(x,5,check)
c         if(ipar.ge.13)CALL newt(x,6,check)
         if(gdeln.eq.0.d0)CALL newt(x,5,check)
         if(gdeln.ne.0.d0)CALL newt(x,6,check)
         IF(check)PAUSE 'There is no root in broydn...'
         CALL mapping(x,rmun,rmue,vsigma,vomega,vrho,vdelta,vphi)
        write(6,*)'rho,fvec=',rnbt/(hbc/rm)**3,(fvec(j),j=1,7)
         do j=1,6
            if(lll(j).eq.0.and.rnb(2+j).gt.1.d-15)then
               rnbc(j)=rnbt
               lll(j)=1
            endif
         enddo
         if(i.gt.1)then
            dpde=(press-pressold)/(ener-enerold)
            pressold=press
            enerold=ener
         endif
         vs2=dpde
         gamma=(press+ener)/press*dpde
         RNBTD=RNBT*(RM/HBC)**3
         WRITE(1,*)rnbtd/denss,-schargeb/3.0D0
         DENER=ENER/RNBT-1.0D0
         ENER=ENER*RM*(RM/HBC)**3
         PRESS=PRESS*RM*(RM/HBC)**3
         bb=(RM/HBC)**3
         WRITE(7,*) RNBTD,ENER/HBC,PRESS/HBC,-schargeb*bb
c         WRITE(77,*) RNBTD,ENER,PRESS,rnl/rnbt,rnb/rnbt,rmef*rm,
c     1        rmuba*rm,rmue*rm,-schargeb*bb
         if(i.gt.1)WRITE(77,*) RNBTD,ENER,PRESS,rnl/rnbt
     1    ,rnb(1)/rnbt,rnb(2)/rnbt,rmef(1)*rm,rmef(2)*rm,
     1       rmuba(1)*rm, rmuba(2)*rm,rmue*rm,vs2,gamma
c        for  Morgane - CompOSE
         WRITE(2,*)rnbtd,rnb/rnbt,rnl/rnbt,rmuba*rm,rmue*rm
         rmns=rmb(1)-vsigma
         WRITE(3,*)RNBTD/DENSS,RMNS,VSIGMA,VOMEGA,
     &        -VRHO,VSIGMAS,VPHI,RMUN,RMUE 
         ENERlep=ENERlep*RM*(RM/HBC)**3
         PRESSlep=PRESSlep*RM*(RM/HBC)**3
         durca=1.d0/(1.d0+(1.d0+(rnl(1)/(rnl(1)+rnl(2)))**(1/3.d0))**3)
C     OUTPUT IN MEV^4 FOR THE PROGRAM THAT CALCULATES STARS PROPERTIES; 
C     IF YOU CHOOSE THIS OUTPUT, COMMENT THE ABOVE ONE
         durca1=(1.d0/(1.d0+(1.d0+(rnl(1)/
     1        (rnl(1)+rnl(2)+rnb(8)+rnb(6)-rnb(4)))**(1/3.d0))**3))
     1        /(rnb(2)/(rnb(2)+rnb(1)))
         rho_hyp=rnb(3)+rnb(4)+rnb(5)+rnb(6)+rnb(7)+rnb(8)
         durca2=((1.d0-rho_hyp/rnbt)/(1.d0+(1.d0+(rnl(1)/
     1        (rnl(1)+rnl(2)+rnb(8)+rnb(6)-rnb(4)))**(1/3.d0))**3))
     1        /(rnb(2)/rnbt)
      if(lll(7).eq.0.and.durca1.le.1.d0)then
               rnbc(7)=rnbt
               lll(7)=1
            endif


         write(78,*)rnbtd,durca/(rnb(2)/rnbt),rnb(1)*bb,
     1        rnb(2)*bb, rnb(3)*bb,rnb(8)*bb,
     1        rnb(7)*bb,rnb(6)*bb,rnb(5)*bb,rnb(4)*bb,rnl(1)*bb,
     2        rnl(2)**2,ener,press,rmun*rm,rmef*rm

cx, n_B, n_n, n_Lambda,
c n_p,n_xi-,n_xi+,nsigma-,nsigma0,nsigma+,ne,nmuon,c_min(i.e. the minimal
c eigenvalue), energy density, pressure, mu_B, mu_q, mu_s,
c mu_e,sigma,omega,rho,phi,sigma^*,x
         WRITE(4,*)RNBTD,DENER,ENER,PRESS,enerlep,presslep,rmun*rm
         PRESS=PRESS/HBC
         ENER=ENER/HBC
      ENDDO
      write(88,*)ipar,usig,rnbc*(RM/HBC)**3
      do i=1,7
         lll(i)=0
         rnbc(i)=rhoc
      enddo
      enddo
      write(6,*)'input TOV'      
      write(6,*)'fort.7:rho,energy_dens,pressure (fm^-4)'
      write(6,*)'densities/fraction of particles'
      write(6,*)'fort.2: rho,YB(8),Ye,Ymu,mu_B(8),mu_e'
      write(6,*)' 1=neutron,2=proton,3=lambda,4=sigma+,5=sigma0,6=sigma-
     1     ,7=cascade0,8=cascade-
     2     =electron,2=muon'
 10   FORMAT(2x,i2,2x,11(1x,e12.5)) 
 11   FORMAT(5(2x,f20.10))
      STOP
      END
c--------------------------------------------------------------------------
      SUBROUTINE mapping(x,rmun,rmue,vsigma,vomega,vrho,vdelta,vphi)
C     This SUBROUTINE sets the potential fields between the physical values    

      IMPLICIT DOUBLE PRECISION(A-H,O-Z)   
      DIMENSION X(7)
      rmun=x(1)**2                            !to assure kfe greater than zero
      rmue=dabs(x(2))!**2                         !to assure kfn greater than zero
      vsigma=dSIN(x(3))**2   !mapping vsigma in (0,mb(1))
      vomega=x(4)**2                       !to assure vomega greater than zero
      vrho=x(5)!no mapping on vrho
      vdelta=x(6)!dSIN(x(6))**2
      vphi=x(7)                 !no mapping on vphi
      vsigmas=0.d0              !dsin(x(7))**2  !dabs(x(6))mapping vsigmas in (0,mb(1))
      RETURN
      END
C-----------------------------------------------------------------------
      SUBROUTINE funcv(n,x,fvec)
C     This SUBROUTINE is used by NEWT and gives the functions to be zeroed 
C     in the vector fvec

      IMPLICIT DOUBLE PRECISION(A-H,O-Z)   
      DIMENSION X(7),FVEC(7),FVEC1(7),SB(8),rmuba(8),rnua(8)
      DIMENSION RMB(8),RML(2),QB(8),RI3(8),GS(8),GV(8),GR(8),GSS(8)
     &,Gphi(8)
      real*8 RNB(8),RNL(2),rmef(8),ri3d(8),rmdel,gdel(8)
      COMMON/CDATAQ/PI2,g,hbc,rm,ipar
      COMMON/CDATA/RMB,RML,RMS,RMV,RMR,RMSS,RMphi,rmdel,RB,RC,RXI,rlv,
     &             GS,GV,GR,GSS,Gphi,QB,RI3,GDEL,RI3D,gdeln
      COMMON/CNBT/RNBT,RNL,SB,SCHARGEB
      COMMON/CFVEC/FVEC1
      COMMON/F/RMA,RNU
      common/lep/enerlep,presslep,ener,press,rnb,rmuba,dpressf,denerf
      common/rmu/rmef,rmule,rnua
      EXTERNAL F1,f3,f4

      CALL mapping(x,rmun,rmue,vsigma,vomega,vrho,vdelta,vphi)
      if(gdeln.eq.0.d0)vdelta=0.d0
      fsigma=0.D0
      fomega=0.D0
      fdelta=0.D0
      frho=0.D0
      fsigmas=0.D0
      fphi=0.D0       
      charge=0.D0                           !electric charge density
      schargeb=0.D0                          
      rnumber=0.D0                           
      fsigmanl=-(gs(1)/rms)**2*(rb*rmb(1)*vsigma**2+rc*vsigma**3)
      fomeganl=0.d0! 
      fsigmasnl=0.0d0      
      fphinl=0.0d0
      fsv=rlv*vomega**2
      press_svr=vrho**2*fsv
      ener_svr=-vrho**2*fsv
      pressf=0.d0
      press=0.d0
      vsigmas=0
c     
      ENERF=(rms*vsigma/gs(1))**2/2.0d0+rb*vsigma**3/3.0d0
     &     +rc*vsigma**4/4.0d0+(rmv*vomega/gv(1))**2/2.0d0
     &     +rxi*vomega**4/8.0d0+(rmr*vrho/gr(1))**2/2.0d0
     &     +(rmss*vsigmas/gss(3))**2/2.0d0
     &     +(rmphi*vphi/gphi(3))**2/2.0d0
     &     +3*rlv*vrho**2*vomega**2
     &  +RMDEL**2*vDELTA**2/2.D0/gdel(1)**2
     
      PRESSF=-(rms*vsigma/gs(1))**2/2.0d0-rb*vsigma**3/3.0d0
     &     -rc*vsigma**4/4.0d0+(rmv*vomega/gv(1))**2/2.0d0
     &     +rxi*vomega**4/24.0d0+(rmr*vrho/gr(1))**2/2.0d0
     &     -(rmss*vsigmas/gss(3))**2/2.0d0
     &     +(rmphi*vphi/gphi(3))**2/2.0d0
     &     +rlv*vrho**2*vomega**2     
     &  -RMDEL**2*vDELTA**2/2.D0/gdel(1)**2

      ENERBAR=0.D0
      PRESSBAR=0.D0
      densb=0.d0
      rkfb=0.d0
      vomega_rho=0.d0
      vrho_rho=0.d0
      vphi_rho=0.d0
      xmuh=0.d0
      do i=1,8
         rnb(i)=0.d0
         rmef(i)=0.d0
         rmuba(i)=0.d0
      enddo

      DO I=1,2!8
      rmub=rmun-qb(i)*rmue 
      rmuba(i)=rmub                        !baryon chemical potential
      if(gdeln.ne.0.d0)then
         rmbs=rmb(i)-vsigma*gs(i)/gs(1)
     1     -vdelta*ri3d(i)*gdel(i)/gdel(1) !vsigmas*gss(i)/gss(3)
      else
         rmbs=rmb(i)-vsigma*gs(i)/gs(1)
      endif
      rma=rmbs
      rnu=rmub-gv(i)/gv(1)*vomega-gr(i)/gr(1)*ri3(i)*vrho
c     &     -gphi(i)/gphi(3)*vphi
      rnua(i)=rnu
      rkfb2=rnu**2-rmbs**2  !baryon fermi mom squared
      IF(rkfb2.GT.0.d0)THEN                                  
         rkfb=dSQRT(rkfb2)     
         else
         rkfb=0.d0
      endif
      rmef(i)=rmbs     
      efb=dSQRT(rkfb**2+rmbs**2)     !baryon fermi energy
      rint=0.5d0*(rkfb*efb-rmbs**2*dLOG((rkfb+efb)/rmbs))   
      rma=rmbs
      densb=rkfb**3/3.d0/pi2
      CALL GAUSS(F1,0.D0,rkfb,20,RE1,II)
      
!      rms2=rms**2+rb*vsigma*gs(1)**2+rc*vsigma**2*gs(1)**2
      rmrho2=rmr**2+2*rlv*gr(1)**2*vomega**2
      rmv2=rmv**2+2*rlv*gv(1)**2*vrho**2
     &+rxi*(gv(1))**2*vomega**2/6.0d0
  
      fsigma=fsigma+gs(i)*gs(1)/rms**2*re1
c      fsigmas=fsigmas+gss(i)*gss(3)/rmss**2*re1
      fomega=fomega+gv(i)*gv(1)/rmv2*densb
      frho=frho+ri3(i)*gr(i)*gr(1)/rmrho2*densb 
c      fphi=fphi+gphi(i)*gphi(3)/rmphi**2*densb
      fdelta=fdelta+ri3d(i)*gdel(i)*gdel(1)/rmdel**2*re1
      
      charge=charge+qb(i)*densb      
      schargeb=schargeb+sb(i)*densb
      rnumber=rnumber+densb
      rnb(i)=densb 
      
      CALL GAUSS(F3,0.D0,rkfb,10,RE3,II)
      CALL GAUSS(F4,0.D0,rkfb,10,RE4,II)
      enerbar=enerbar+re3
      pressbar=pressbar+re4
      ENDDO  
c     
c---------------------------------------
c     leptons
c     
      enerlep=0.d0
      presslep=0.d0
      chargel=0.d0
      xmul=0.d0
      do i=1,2
      rkfe2=rmue**2-rml(i)**2
      IF(rkfe2.GT.0.d0)THEN                                  
         rkfe=dSQRT(rkfe2)     
         else
         rkfe=0.d0
      endif     
      dense=rkfe**3/3.d0/pi2
      charge=charge-dense
      rnl(i)=dense
      RNU=RMUE      
      RMA=RML(i)
      CALL GAUSS(F3,0.D0,rkfe,10,RE3Le,II)
      ENERLEP=ENERLEP+RE3Le
      CALL GAUSS(F4,0.D0,rkfe,10,RE4Le,II)
      PRESSLEP=PRESSLEP+RE4Le
      enddo

      ener=enerf+enerbar+enerlep
      press=pressf+pressbar+presslep

      FSIGMA=FSIGMA+FSIGMANL
      FSIGMAS=FSIGMAS+FSIGMASNL
      Fphi=Fphi+FphiNL      
      FVEC(1)=FSIGMA-VSIGMA
      FVEC(2)=FOMEGA-VOMEGA
      FVEC(3)=FRHO-VRHO
      FVEC(4)=CHARGE
      FVEC(5)=RNUMBER-RNBT
      FVEC(6)=Fdelta-Vdelta         
      FVEC(7)=Fphi-Vphi      
      DO I=1,7
         FVEC1(I)=FVEC(I) 
      ENDDO
c      write(6,*)x
c      write(6,*)vsigma,vomega,vrho,vdelta
c       if(ipar.le.12)write(6,*)(fvec(i),i=1,5)
c       if(ipar.ge.13)write(6,*)(fvec(i),i=1,6)
        
      RETURN
      END      
C-----------------------------------------------------------------------
      FUNCTION F1(X)
      IMPLICIT DOUBLE PRECISION(A-H,O-Z)   
      DATA PI2/9.86960441009D0/
      COMMON/F/RMA,RNU
      E=DSQRT(X*X+RMA*RMA)
      F1=X*X/E*RMA/PI2
      
      RETURN
      END
C------------------------------------------------------------------
      FUNCTION F3(X)
      IMPLICIT DOUBLE PRECISION(A-H,O-Z)   
      COMMON/F/RMA,RNU
      DATA PI2/9.86960441009D0/

      E=DSQRT(X*X+RMA*RMA)
      F3=X*X*E/PI2

      RETURN
      END

C--------------------------------------------------------
      FUNCTION F4(X)
      IMPLICIT DOUBLE PRECISION(A-H,O-Z)   
      COMMON/F/RMA,RNU
      DATA PI2/9.86960441009D0/

      E=DSQRT(X*X+RMA*RMA)
      F4=X**4/E/(3.D0*PI2)

      RETURN
      END
C---------------------------------------------------------------
        SUBROUTINE GAUSS(F,UG,OG,NN,FXINT,II)
        IMPLICIT DOUBLE PRECISION(A-H,O-Z)
        DIMENSION WG(10),ZG(10)
        DATA WG/0.6667134430869 D-01,
     C  0.1494513491506D00,
     C  0.2190863625160D00,
     C  0.2692667193100D00,
     C  0.2955242247148D00,
     C  0.2955242247148D00,
     C  0.2692667193100D00,
     C  0.2190863625160D00,
     C  0.1494513491506D00,
     C           0.6667134430869D-01/
        DATA ZG/-0.9739065285172D00,
     C  -0.8650633666890D00,
     C  -0.6794095682990D00,
     C  -0.4333953941292D00,
     C  -0.1458743389816D00,
     C  +0.1458743389816D00,
     C  +0.4333953941292D00,
     C  +0.6794095682990D00,
     C  +0.8650633666890D00,
     C          +0.9739065285172D00/

        FXINT=0.D0
        HH=(OG-UG)/DBLE(FLOAT(NN))
        U=UG
        O=U+HH
        KK=1
24      OU=O+U
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
C=======================================================================
C     Other subroutines from Numerical Recipes
C=======================================================================

C ... Given an initial guess x(1:n) for a root in n dimensions, find the root by a
C ... globally convergent Newton's method. The vector of functions to be zeroed,
C ... called fvec(1:n) in the routine below, is returned by a user-supplied
C ... subroutine that must be called funcv and have the declaration subroutine
C ... funcv(n,x,fvec). The output quantity check is false on a normal return and
C ... true if the routine has converged to a local minimum of the function fmin
C ... defined below. In this case try restarting from a different initial guess.
C ... Parameters: NP is the maximum expected value of n; MAXITS is the maximum
C ... number of iterations; TOLF sets the convergence criterion on function
C ... values; TOLMIN sets the criterion for deciding whether spurious convergence
C ... to a minimum of fmin has occurred; TOLX is the convergence criterion on ffix;
C ... STPMX is the scaled maximum step length allowed in line searches. 


      SUBROUTINE newt(x,n,check) 
      INTEGER n,nn,NP,MAXITS 
      LOGICAL check 
      REAL*8 x(n),fvec,TOLF,TOLMIN,TOLX,STPMX 

      PARAMETER(NP=40,MAXITS=2000,TOLF=1.e-10,TOLMIN=1.e-12,TOLX=1.e-12, 
     &          STPMX=100.)
c      PARAMETER(NP=40,MAXITS=2000,TOLF=1.e-10,TOLMIN=1.e-12,TOLX=1.e-12, 
c     &          STPMX=100.)
c      PARAMETER (NP=40,MAXITS=200,TOLF=1.e-4,TOLMIN=1.e-6,TOLX=1.e-7, 
c     &          STPMX=100.)

      COMMON /newtv/ fvec(NP),nn 
      SAVE /newtv/ 

c ... test

      common/iter/its 

c ... 



C USES fdjac,fmin,lnsrch,lubksb,ludcmp


      INTEGER i,its,j,indx(NP) 
      REAL*8 d,den,f,fold,stpmax,sum,temp,test,fjac(NP,NP), 
     & g(NP),p(NP),xold(NP),fmin

      EXTERNAL fmin 

      nn=n 

      f=fmin(x) 
      test=0. 

      do 11 i=1,n 
      if(abs(fvec(i)).gt.test) test=abs(fvec(i)) 
 11   continue

      if(test.lt..01*TOLF) then
      check=.false. 
      return 
      endif 
      sum=0. 

      do 12 i=1,n
      sum=sum+x(i)**2 
 12   continue
 
      stpmax=STPMX*max(sqrt(sum),float(n)) 
      do 21 its=1,MAXITS 

      call fdjac(n,x,fvec,NP,fjac) ! Numerical
c      call fdjac(n,x,fjac) ! Analytical

      do 14 i=1,n 
      sum=0. 
      do 13 j=1,n
      sum=sum+fjac(j,i)*fvec(j) 
 13   continue
      g(i)=sum 
 14   continue
      do 15 i=1,n 
      xold(i)=x(i) 
 15   continue
      fold=f 
      do 16 i=1,n 
      p(i)=-fvec(i) 
 16   continue

      call dludcmp(fjac,n,NP,indx,d)
      call dlubksb(fjac,n,NP,indx,p) 
      call lnsrch(n,xold,fold,g,p,x,f,stpmax,check,fmin)

      test=0. 
      do 17 i=1,n

      if(abs(fvec(i)).gt.test) test=abs(fvec(i)) 

 17   continue 

      if(test.lt.TOLF) then
       check=.false. 
      return 
      endif 
      if(check)then 
      test=0. 
      den=max(f,.5*n) 
      do 18 i=1,n
      temp=abs(g(i))*max(abs(x(i)),1.)/den 
      if(temp.gt.test)test=temp 
18    continue
      if(test.lt.TOLMIN)then
      check=.true. 
      else
      check=.false. 
      endif 
      return

      endif 
      test=0. 

      do 19 i=1,n
      temp=(abs(x(i)-xold(i)))/max(abs(x(i)),1.) 
      if(temp.gt.test)test=temp 
 19   continue
      if(test.lt.TOLX) return 
 21   continue 
      pause 'MAXITS exceeded in newt' 
      return
      END



      SUBROUTINE broydn(x,n,check)
      INTEGER n,nn,NP,MAXITS
      DOUBLE PRECISION x(n),fvec,EPS,TOLF,TOLMIN,TOLX,STPMX
      LOGICAL check
      PARAMETER (NP=40,MAXITS=2000,EPS=3.d-12,TOLF=1.e-6,TOLMIN=1.e-12
     &     ,TOLX=EPS,  STPMX=100.)
c      PARAMETER (NP=40,MAXITS=40000,EPS=3.d-16,TOLF=1.d-12,
c     &TOLMIN=1.d-12,TOLX=EPS,STPMX=100.d0)
      COMMON /newtv/ fvec(NP),nn
      SAVE/newtv/
CU    USES fdjac,fmin,lnsrch,qrdcmp,qrupdt,rsolv
      INTEGER i,its,j,k
      DOUBLE PRECISION den,f,fold,stpmax,sum,temp,test,c(NP),d(NP)
     *,fvcold(NP),g(NP),
     *p(NP),qt(NP,NP),r(NP,NP),s(NP),t(NP),w(NP),xold(NP),fmin
      LOGICAL restrt,sing,skip
      EXTERNAL fmin
      nn=n
      f=fmin(x)
      test=0.d0
      do 11 i=1,n
        if(abs(fvec(i)).gt.test)test=abs(fvec(i))
11    continue
      if(test.lt..01d0*TOLF)then
        check=.false.
        return
      endif
      sum=0.d0
      do 12 i=1,n
        sum=sum+x(i)**2
12    continue
      stpmax=STPMX*max(sqrt(sum), dble(n))
      restrt=.true.
      do 44 its=1,MAXITS
        if(restrt)then
          call fdjac(n,x,fvec,NP,r)
          call qrdcmp(r,n,NP,c,d,sing)
          if(sing) pause 'singular Jacobian in broydn'
          do 14 i=1,n
            do 13 j=1,n
              qt(i,j)=0.d0
13          continue
            qt(i,i)=1.d0
14        continue
          do 18 k=1,n-1
            if(c(k).ne.0.d0)then
              do 17 j=1,n
                sum=0.d0
                do 15 i=k,n
                  sum=sum+r(i,k)*qt(i,j)
15              continue
                sum=sum/c(k)
                do 16 i=k,n
                  qt(i,j)=qt(i,j)-sum*r(i,k)
16              continue
17            continue
            endif
18        continue
          do 21 i=1,n
            r(i,i)=d(i)
            do 19 j=1,i-1
              r(i,j)=0.d0
19          continue
21        continue
        else
          do 22 i=1,n
            s(i)=x(i)-xold(i)
22        continue
          do 24 i=1,n
            sum=0.d0
            do 23 j=i,n
              sum=sum+r(i,j)*s(j)
23          continue
            t(i)=sum
24        continue
          skip=.true.
          do 26 i=1,n
            sum=0.d0
            do 25 j=1,n
              sum=sum+qt(j,i)*t(j)
25          continue
            w(i)=fvec(i)-fvcold(i)-sum
            if(abs(w(i)).ge.EPS*(abs(fvec(i))+abs(fvcold(i))))then
              skip=.false.
            else
              w(i)=0.d0
            endif
26        continue
          if(.not.skip)then
            do 28 i=1,n
              sum=0.d0
              do 27 j=1,n
                sum=sum+qt(i,j)*w(j)
27            continue
              t(i)=sum
28          continue
            den=0.d0
            do 29 i=1,n
              den=den+s(i)**2
29          continue
            do 31 i=1,n
              s(i)=s(i)/den
31          continue
            call qrupdt(r,qt,n,NP,t,s)
            do 32 i=1,n
              if(r(i,i).eq.0.d0) pause 'r singular in broydn'
              d(i)=r(i,i)
32          continue
          endif
        endif
        do 34 i=1,n
          sum=0.d0
          do 33 j=1,n
            sum=sum+qt(i,j)*fvec(j)
33        continue
          g(i)=sum
34      continue
        do 36 i=n,1,-1
          sum=0.d0
          do 35 j=1,i
            sum=sum+r(j,i)*g(j)
35        continue
          g(i)=sum
36      continue
        do 37 i=1,n
          xold(i)=x(i)
          fvcold(i)=fvec(i)
37      continue
        fold=f
        do 39 i=1,n
          sum=0.d0
          do 38 j=1,n
            sum=sum+qt(i,j)*fvec(j)
38        continue
          p(i)=-sum
39      continue
        call rsolv(r,n,NP,d,p)
        call lnsrch(n,xold,fold,g,p,x,f,stpmax,check,fmin)
        test=0.d0
        do 41 i=1,n
          if(abs(fvec(i)).gt.test)test=abs(fvec(i))
41      continue
        if(test.lt.TOLF)then
          check=.false.
          return
        endif
        if(check)then
          if(restrt)then
            return
          else
            test=0.d0
            den=max(f,.5d0*n)
            do 42 i=1,n
              temp=abs(g(i))*max(abs(x(i)),1.d0)/den
              if(temp.gt.test)test=temp
42          continue
            if(test.lt.TOLMIN)then
              return
            else
              restrt=.true.
            endif
          endif
        else
          restrt=.false.
          test=0.d0
          do 43 i=1,n
            temp=(abs(x(i)-xold(i)))/max(abs(x(i)),1.d0)
            if(temp.gt.test)test=temp
43        continue
          if(test.lt.TOLX)return
        endif
44    continue
c      pause 'MAXITS exceeded in broydn'
      Write(*,*)'MAXITS exceeded in broydn'
      stop
      END
C-----------------------------------------------------------------------
      SUBROUTINE fdjac(n,x,fvec,np,df)
      INTEGER n,np,NMAX
      DOUBLE PRECISION df(np,np),fvec(n),x(n),EPS
      PARAMETER (NMAX=40,EPS=1.d-7 ) !estava EPS=1.d-8
CU    USES funcv
      INTEGER i,j
      DOUBLE PRECISION h,temp,f(NMAX)!,rmun,rmuc,rmus,rhs
c      common/rmu/rmun,rmuc,rmus,rhs,rhq,rmef
      do 12 j=1,n
        temp=x(j)
        h=EPS*abs(temp)
        if(h.eq.0.d0)h=EPS
        x(j)=temp+h
        h=x(j)-temp
        call funcv(n,x,f)
        x(j)=temp
        do 11 i=1,n
          df(i,j)=(f(i)-fvec(i))/h
11      continue
c      if(dabs(rhs).lt.1.d-7)then
c       df(8,8)=1.d0
c      endif
12    continue
      return
      END
C-----------------------------------------------------------------------
      FUNCTION fmin(x)
      INTEGER n,NP
      DOUBLE PRECISION fmin,x(*),fvec
      PARAMETER (NP=40)
      COMMON /newtv/ fvec(NP),n
      SAVE /newtv/
CU    USES funcv
      INTEGER i
      DOUBLE PRECISION sum
      call funcv(n,x,fvec)
      sum=0.d0
      do 11 i=1,n
        sum=sum+fvec(i)**2
11    continue
      fmin=0.5d0*sum
      return
      END
C-----------------------------------------------------------------------
      SUBROUTINE lnsrch(n,xold,fold,g,p,x,f,stpmax,check,func)
      INTEGER n
      LOGICAL check
      DOUBLE PRECISION f,fold,stpmax,g(n),p(n),x(n),xold(n),func,ALF
     *,TOLX
      PARAMETER (ALF=1.d-4,TOLX=1.d-16)
c      PARAMETER (ALF=1.d-4,TOLX=1.d-16)
      EXTERNAL func
CU    USES func
      INTEGER i
      DOUBLE PRECISION a,alam,alam2,alamin,b,disc,f2,fold2,rhs1,rhs2
     *,slope,sum,temp,
     *test,tmplam
      check=.false.
      sum=0.d0
      do 11 i=1,n
        sum=sum+p(i)*p(i)
11    continue
      sum=sqrt(sum)
      if(sum.gt.stpmax)then
        do 12 i=1,n
          p(i)=p(i)*stpmax/sum
12      continue
      endif
      slope=0.d0
      do 13 i=1,n
        slope=slope+g(i)*p(i)
13    continue
      test=0.d0
      do 14 i=1,n
        temp=abs(p(i))/max(abs(xold(i)),1.d0)
        if(temp.gt.test)test=temp
14    continue
      alamin=TOLX/test
      alam=1.d0
1     continue
        do 15 i=1,n
          x(i)=xold(i)+alam*p(i)
15      continue
        f=func(x)
        if(alam.lt.alamin)then
          do 16 i=1,n
            x(i)=xold(i)
16        continue
          check=.true.
          return
        else if(f.le.fold+ALF*alam*slope)then
          return
        else
          if(alam.eq.1.d0)then
            tmplam=-slope/(2.d0*(f-fold-slope))
          else
            rhs1=f-fold-alam*slope
            rhs2=f2-fold2-alam2*slope
            a=(rhs1/alam**2-rhs2/alam2**2)/(alam-alam2)
            b=(-alam2*rhs1/alam**2+alam*rhs2/alam2**2)/(alam-alam2)
            if(a.eq.0.d0)then
              tmplam=-slope/(2.d0*b)
            else
              disc=b*b-3.d0*a*slope
              if(disc.lt.0.d0) pause 'roundoff problem in lnsrch'
              tmplam=(-b+sqrt(disc))/(3.d0*a)
            endif
            if(tmplam.gt..5d0*alam)tmplam=.5d0*alam
          endif
        endif
        alam2=alam
        f2=f
        fold2=fold
        alam=max(tmplam,.1d0*alam)
      goto 1
      END
C-----------------------------------------------------------------------
      SUBROUTINE qrdcmp(a,n,np,c,d,sing)
      INTEGER n,np
      DOUBLE PRECISION a(np,np),c(n),d(n)
      LOGICAL sing
      INTEGER i,j,k
      DOUBLE PRECISION scale,sigma,sum,tau
      sing=.false.
      do 17 k=1,n-1
        scale=0.d0
        do 11 i=k,n
          scale=max(scale,abs(a(i,k)))
11      continue
        if(scale.eq.0.d0)then
          sing=.true.
          c(k)=0.d0
          d(k)=0.d0
        else
          do 12 i=k,n
            a(i,k)=a(i,k)/scale
12        continue
          sum=0.d0
          do 13 i=k,n
            sum=sum+a(i,k)**2
13        continue
          sigma=sign(sqrt(sum),a(k,k))
          a(k,k)=a(k,k)+sigma
          c(k)=sigma*a(k,k)
          d(k)=-scale*sigma
          do 16 j=k+1,n
            sum=0.d0
            do 14 i=k,n
              sum=sum+a(i,k)*a(i,j)
14          continue
            tau=sum/c(k)
            do 15 i=k,n
              a(i,j)=a(i,j)-tau*a(i,k)
15          continue
16        continue
        endif
17    continue
      d(n)=a(n,n)
      if(d(n).eq.0.d0)sing=.true.
      return
      END
C-----------------------------------------------------------------------
      SUBROUTINE qrupdt(r,qt,n,np,u,v)
      INTEGER n,np
      DOUBLE PRECISION r(np,np),qt(np,np),u(np),v(np)
CU    USES rotate
      INTEGER i,j,k
      do 11 k=n,1,-1
        if(u(k).ne.0.d0)goto 1
11    continue
      k=1
1     do 12 i=k-1,1,-1
        call rotate(r,qt,n,np,i,u(i),-u(i+1))
        if(u(i).eq.0.d0)then
          u(i)=abs(u(i+1))
        else if(abs(u(i)).gt.abs(u(i+1)))then
          u(i)=abs(u(i))*sqrt(1.d0+(u(i+1)/u(i))**2)
        else
          u(i)=abs(u(i+1))*sqrt(1.d0+(u(i)/u(i+1))**2)
        endif
12    continue
      do 13 j=1,n
        r(1,j)=r(1,j)+u(1)*v(j)
13    continue
      do 14 i=1,k-1
        call rotate(r,qt,n,np,i,r(i,i),-r(i+1,i))
14    continue
      return
      END
C-----------------------------------------------------------------------
      SUBROUTINE rsolv(a,n,np,d,b)
      INTEGER n,np
      DOUBLE PRECISION a(np,np),b(n),d(n)
      INTEGER i,j
      DOUBLE PRECISION sum
      b(n)=b(n)/d(n)
      do 12 i=n-1,1,-1
        sum=0.d0
        do 11 j=i+1,n
          sum=sum+a(i,j)*b(j)
11      continue
        b(i)=(b(i)-sum)/d(i)
12    continue
      return
      END
C-----------------------------------------------------------------------
      SUBROUTINE rotate(r,qt,n,np,i,a,b)
      INTEGER n,np,i
      DOUBLE PRECISION a,b,r(np,np),qt(np,np)
      INTEGER j
      DOUBLE PRECISION c,fact,s,w,y
      if(a.eq.0.d0)then
        c=0.d0
        s=sign(1.d0,b)
      else if(abs(a).gt.abs(b))then
        fact=b/a
        c=sign(1.d0/sqrt(1.d0+fact**2),a)
        s=fact*c
      else
        fact=a/b
        s=sign(1.d0/sqrt(1.d0+fact**2),b)
        c=fact*s
      endif
      do 11 j=i,n
        y=r(i,j)
        w=r(i+1,j)
        r(i,j)=c*y-s*w
        r(i+1,j)=s*y+c*w
11    continue
      do 12 j=1,n
        y=qt(i,j)
        w=qt(i+1,j)
        qt(i,j)=c*y-s*w
        qt(i+1,j)=s*y+c*w
12    continue
      return
      END
C========================================================================
      SUBROUTINE JACOBI(A,N,NP,D,V,NROT)

C  Purpose: Computes all eigenvalues and eigenvectors of a real
C     symmetric matrix A, which is of size N by N, stored in a
C     physical NP by NP array.  On output, elements of A above the
C     diagonal are destroyed.  D returns the eigenvalues of A in
C     its first N elements.  V is a matrix with the same logical and
C     physical dimensions as A whose columns contain, on output, the
C     normalized eigenvectors of A.  NROT returns the number of Jacobi
C     rotations which were required. 

C  Source: W. H. Press et al., "Numerical Recipes", 1989, p. 346.

C  Modifications:

C     1. Double precision version

C  Prepared by J. Applequist, 10/23/91

      IMPLICIT REAL*8(A-H,O-Z)
      PARAMETER (NMAX=100)
      DIMENSION A(NP,NP),D(NP),V(NP,NP),B(NMAX),Z(NMAX)

C     Initialize the identity matrix.

      DO 12 IP=1,N
      DO 11 IQ=1,N
      V(IP,IQ)=0.D0
 11   CONTINUE
      V(IP,IP)=1.D0
 12   CONTINUE

C     Initialize B and D to the diagonal of A.

      DO 13 IP=1,N
      B(IP)=A(IP,IP)
      D(IP)=B(IP)
      Z(IP)=0.D0
 13   CONTINUE
      NROT=0
      DO 24 I=1,100
      SM=0.D0

C     Sum off-diagonal elements.

      DO 15 IP=1,N-1
      DO 14 IQ=IP+1,N
      SM=SM+DABS(A(IP,IQ))
 14   CONTINUE
 15   CONTINUE
      IF (SM.EQ.0.D0) RETURN
      IF (I.LT.4) THEN
      TRESH=0.2D0*SM/N**2
      ELSE
      TRESH=0.D0
      ENDIF
      DO 22 IP=1,N-1
      DO 21 IQ=IP+1,N
      G=100.D0*DABS(A(IP,IQ))

C     After four sweeps, skip the rotation if the off-diagonal
C     element is small.

      IF ((I.GT.4).AND.(DABS(D(IP))+G.EQ.DABS(D(IP)))
     &  .AND.(DABS(D(IQ))+G.EQ.DABS(D(IQ)))) THEN
      A(IP,IQ)=0.D0
      ELSE IF (DABS(A(IP,IQ)).GT.TRESH) THEN
        H=D(IQ)-D(IP)
        IF (DABS(H)+G.EQ.DABS(H)) THEN
        T=A(IP,IQ)/H
        ELSE
        THETA=0.5D0*H/A(IP,IQ)
        T=1.D0/(DABS(THETA)+DSQRT(1.D0+THETA**2))
        IF (THETA.LT.0.D0) T=-T
        ENDIF
      C=1.D0/DSQRT(1.D0+T**2)
      S=T*C
      TAU=S/(1.D0+C)
      H=T*A(IP,IQ)
      Z(IP)=Z(IP)-H
      Z(IQ)=Z(IQ)+H
      D(IP)=D(IP)-H
      D(IQ)=D(IQ)+H
      A(IP,IQ)=0.D0
      DO 16 J=1,IP-1
      G=A(J,IP)
      H=A(J,IQ)
      A(J,IP)=G-S*(H+G*TAU)
      A(J,IQ)=H+S*(G-H*TAU)
 16   CONTINUE
      DO 17 J=IP+1,IQ-1
      G=A(IP,J)
      H=A(J,IQ)
      A(IP,J)=G-S*(H+G*TAU)
      A(J,IQ)=H+S*(G-H*TAU)
 17   CONTINUE
      DO 18 J=IQ+1,N
      G=A(IP,J)
      H=A(IQ,J)
      A(IP,J)=G-S*(H+G*TAU)
      A(IQ,J)=H+S*(G-H*TAU)
 18   CONTINUE
      DO 19 J=1,N
      G=V(J,IP)
      H=V(J,IQ)
      V(J,IP)=G-S*(H+G*TAU)
      V(J,IQ)=H+S*(G-H*TAU)
 19   CONTINUE
      NROT=NROT+1
      ENDIF
 21   CONTINUE
 22   CONTINUE
      DO 23 IP=1,N
      B(IP)=B(IP)+Z(IP)
      D(IP)=B(IP)
      Z(IP)=0.D0
 23   CONTINUE
 24   CONTINUE
      WRITE (6,600) 
 600  FORMAT(/'50 ITERATIONS OCCURRED IN SUBROUTINE JACOBI.')
      RETURN
      END
c--------------
      SUBROUTINE EIGSRT(D,V,N,NP)
      implicit none
      integer*4 n, np
      real*8    d(np),v(np,np)

c***********************************************************************
C.! ROUTINE: EIGSRT
C.! PURPOSE: This routine given the eigenvalues and eigenvectors
C.!          sorts the eigenvalues into ascending order, and rearranges the 
C.!          columns of square matrix correspondingly.  The method is straight
C.!          insertion.
C.!
C.!          see pg. 348 w/ explanation pgs.335-376
C.!          Numerical Recipes: The Art of Scientific Programming
C.!          (FORTRAN version), 1st edition
C.!          W.H. Press, B.P. Flannery, S.A. Teukolsky, W.T. Vetterling
C.!          Cambridge Univ. Press., 1986
C.!
c***********************************************************************

      integer*4 i,j,k
      real*8    p

      do 13 i=1,n-1
        k = i
        p = d(i)
        do j=i+1,n
          if(d(j).ge.p) then
            k = j
            p = d(j)
          end if
        enddo
        if( k .ne. i ) then
          d(k) = d(i)
          d(i) = p
          do j = 1,n
            p = v(j,i)
            v(j,i) = v(j,k)
            v(j,k) = p
          enddo
        end if
  13  continue

      return
      end
c -------    c-
      	SUBROUTINE DLUDCMP(A,N,NP,INDX,D)
C................................................................
C	Given a NxN matrix A, with PHYSICAL dimension NP
C	the routine replaces it by its Lower-Upper LU
C	decomposition, with a row-wise ordering given by
C	INDX (dimensioned at N) and sign exchange D
C	Used with DLUBKSB to solve linear systems or
C	inverting a matrix
C
C	Parameters
C	A	matrix dimensioned at (NP,NP), logical NxN
c	INDX	integer array dimensioned to N at least
C	D	Real*8 number indicating the sign of permutations
C
C	Limitations: N max is 250
C
C	A is destroyed
C................................................................
C
      IMPLICIT REAL*8 (A-H,O-Z)
	     PARAMETER (NMAX=250,TINY=1.0D-20)
	     DIMENSION A(NP,NP),INDX(N),VV(NMAX)
	     D=1.D0
	     DO 12 I=1,N
	     AAMAX=0.D0
	     DO 11 J=1,N
	     IF (ABS(A(I,J)).GT.AAMAX) AAMAX=ABS(A(I,J))
   11	CONTINUE
	     IF (AAMAX.EQ.0.D0) PAUSE 'Singular matrix.'
	     VV(I)=1.D0/AAMAX
   12	CONTINUE
	     DO 19 J=1,N
	     IF (J.GT.1) THEN
	     DO 14 I=1,J-1
	     SUM=A(I,J)
	     IF (I.GT.1)THEN
	     DO 13 K=1,I-1
	     SUM=SUM-A(I,K)*A(K,J)
   13	CONTINUE
	     A(I,J)=SUM
	     ENDIF
   14	CONTINUE
	     ENDIF
	     AAMAX=0.D0
	     DO 16 I=J,N
	     SUM=A(I,J)
	     IF (J.GT.1)THEN
	     DO 15 K=1,J-1
	     SUM=SUM-A(I,K)*A(K,J)
   15	CONTINUE
	     A(I,J)=SUM
	     ENDIF
	     DUM=VV(I)*ABS(SUM)
	     IF (DUM.GE.AAMAX) THEN
	     IMAX=I
	     AAMAX=DUM
	     ENDIF
   16	CONTINUE
	     IF (J.NE.IMAX)THEN
	     DO 17 K=1,N
	     DUM=A(IMAX,K)
	     A(IMAX,K)=A(J,K)
	     A(J,K)=DUM
   17	CONTINUE
	     D=-D
	     VV(IMAX)=VV(J)
	     ENDIF
	     INDX(J)=IMAX
	     IF(J.NE.N)THEN
	     IF(A(J,J).EQ.0.D0) A(J,J)=TINY
	     DUM=1.D0/A(J,J)
	     DO 18 I=J+1,N
	     A(I,J)=A(I,J)*DUM
   18	CONTINUE
	     ENDIF
   19	CONTINUE
	     IF(A(N,N).EQ.0.D0)A(N,N)=TINY
	     RETURN
	     END
c-------------------
      	SUBROUTINE DLUBKSB(A,N,NP,INDX,B)
C..............................................................
C	Routine to solve the linear system
C	A. X = B
C	where A is the matrix already in LU decomposition form
C	(see DLUDCMP routine)
C	and B is the rhs vector.
C
C	On output, B contains the solution
C
C	The way of solving a system of linear equations is
C	Call DLUDCMP to change A into its LU decomposition
C	call afterwards DLUBCKS (backsubstitution)
C
C	A	dimensioned at (NP,NP), logical NxN
C	INDX	order of rows (see DLUDCMP), dimensioned to N
C	B	Column vector, dimensioned (at least) to N
C
C	A is not destroyed, so this routine may be called
C	many times, per one call of DLUDCMP
C
C..............................................................
	IMPLICIT REAL*8 (A-H,O-Z)
	DIMENSION A(NP,NP),INDX(N),B(N)
	II=0
	DO 12 I=1,N
	LL=INDX(I)
	SUM=B(LL)
	B(LL)=B(I)
	IF (II.NE.0)THEN
	DO 11 J=II,I-1
	SUM=SUM-A(I,J)*B(J)
11	CONTINUE
	ELSE IF (SUM.NE.0.D0) THEN
	II=I
	ENDIF
	B(I)=SUM
12	CONTINUE
	DO 14 I=N,1,-1
	SUM=B(I)
	IF(I.LT.N)THEN
	DO 13 J=I+1,N
	SUM=SUM-A(I,J)*B(J)
13	CONTINUE
	ENDIF
	B(I)=SUM/A(I,I)

14	CONTINUE
	RETURN
	END

c$$$      include 'djacobi.f'
c$$$      include 'deigsrt.f'
c$$$      include 'dludcmp.f'
c$$$      include 'dlubksb.f'
c      include 'newt.f'
