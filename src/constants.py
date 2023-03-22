# Position départ Joueur
POSITION_DEPART = {'Bleu':[0, 0], 'Jaune':[0, 19], 'Vert':[19, 0], 'Rouge':[19, 19]}


# Le nombre de pièce maximal par joueur
MAX_PIECES = 21


PIECES_IMAGES = ["/1.png","/2.png","/3.png",
                "/4.png","/5.png","/6.png",
                "/7.png","/8.png","/9.png",
                "/10.png","/11.png","/12.png",
                "/13.png","/14.png","/15.png",
                "/16.png","/17.png","/18.png",
                "/19.png","/20.png","/21.png"]

URL_BLEU = [
    "https://i.goopics.net/t9htur.png" , "https://i.goopics.net/hf8bny.png", "https://i.goopics.net/bn4d0e.png", "https://i.goopics.net/4uxu23.png", "https://i.goopics.net/cl2x9u.png", "https://i.goopics.net/drdok6.png", "https://i.goopics.net/ad6s8k.png", "https://i.goopics.net/7br0jw.png", "https://i.goopics.net/a977tl.png", "https://i.goopics.net/v6e1vu.png", "https://i.goopics.net/2cc5tl.png", "https://i.goopics.net/i7wa73.png", "https://i.goopics.net/668ilk.png", "https://i.goopics.net/igfxdx.png", "https://i.goopics.net/36byxn.png", "https://i.goopics.net/fg3ltm.png", "https://i.goopics.net/rnms66.png", "https://i.goopics.net/906h6l.png", "https://i.goopics.net/6wy8qa.png", "https://i.goopics.net/52otyq.png", "https://i.goopics.net/s5hc6q.png"]

URL_VERT = [
    "https://i.goopics.net/wq44mx.png", "https://i.goopics.net/n3gbmb.png", "https://i.goopics.net/7miurr.png", "https://i.goopics.net/gga8oc.png", "https://i.goopics.net/0i4aye.png", "https://i.goopics.net/nfspdy.png", "https://i.goopics.net/ec1qrq.png", "https://i.goopics.net/g9snny.png", "https://i.goopics.net/fk3clt.png", "https://i.goopics.net/2cnse1.png", "https://i.goopics.net/n1wf16.png", "https://i.goopics.net/y6jrcm.png", "https://i.goopics.net/kqe4k3.png", "https://i.goopics.net/8ztccs.png", "https://i.goopics.net/1asxm0.png", "https://i.goopics.net/cpwdvl.png", "https://i.goopics.net/ir4o13.png", "https://i.goopics.net/fogia4.png", "https://i.goopics.net/jo7snr.png", "https://i.goopics.net/nx7cxw.png", "https://i.goopics.net/097li7.png"]

URL_JAUNE = [
    "https://i.goopics.net/ycwfhu.png", "https://i.goopics.net/o48h3v.png", "https://i.goopics.net/qwtwra.png", "https://i.goopics.net/a4wtou.png", "https://i.goopics.net/rywedr.png", "https://i.goopics.net/308nbh.png", "https://i.goopics.net/clhyks.png", "https://i.goopics.net/vm8rkz.png", "https://i.goopics.net/056pgi.png", "https://i.goopics.net/pr7qxd.png", "https://i.goopics.net/qegprd.png", "https://i.goopics.net/e5g26a.png", "https://i.goopics.net/x11pkg.png", "https://i.goopics.net/66gilp.png", "https://i.goopics.net/6yc682.png", "https://i.goopics.net/sptbtp.png", "https://i.goopics.net/y9gcpw.png", "https://i.goopics.net/18jgxa.png", "https://i.goopics.net/l64m50.png", "https://i.goopics.net/tc107r.png", "https://i.goopics.net/phe7qi.png"]

URL_ROUGE = [
    "https://i.goopics.net/8lqd5q.png", "https://i.goopics.net/nnhpic.png", "https://i.goopics.net/m6elus.png", "https://i.goopics.net/eqsunt.png", "https://i.goopics.net/mxidup.png", "https://i.goopics.net/tco5at.png", "https://i.goopics.net/a39uqe.png", "https://i.goopics.net/j5p33w.png", "https://i.goopics.net/li4ww0.png", "https://i.goopics.net/oouwd3.png", "https://i.goopics.net/c8jqju.png", "https://i.goopics.net/wnmw9i.png", "https://i.goopics.net/8robo7.png", "https://i.goopics.net/y4rw3r.png", "https://i.goopics.net/k93nz3.png", "https://i.goopics.net/uionwr.png", "https://i.goopics.net/6abz3j.png", "https://i.goopics.net/f8jjot.png", "https://i.goopics.net/xrspd4.png", "https://i.goopics.net/xhh6qp.png", 
    "https://i.goopics.net/tw8ksa.png"
]

PIECES_IMAGES_URL ={ "BLEU" : URL_BLEU, "JAUNE" : URL_JAUNE, "VERT" : URL_VERT, "ROUGE" : URL_ROUGE}

#  list pièce: 
PIECES =    [
                [[1]],                                
                [[1],[1]],                          
                [[1],[1],[1]],                      
                [[1,0],[1,1]],                      
                [[1],[1],[1],[1]],                  
                [[0,1],[0,1],[1,1]],                 
                [[1,0],[1,1],[1,0]],                   
                [[1,1],[1,1]],
                [[0, 1], [1, 1], [1, 0]],                                          
                [[1],[1],[1],[1],[1]],              
                [[0,1],[0,1],[0,1],[1,1]],          
                [[0,1],[0,1],[1,1],[1,0]],          
                [[0,1],[1,1],[1,1]],                                            
                [[1,1],[0,1],[1,1]],             
                [[1,0],[1,1],[1,0],[1,0]],           
                [[0,1,0],[0,1,0],[1,1,1]],            
                [[1,0,0],[1,0,0],[1,1,1]],           
                [[1,1,0],[0,1,1],[0,0,1]],        
                [[1,0,0],[1,1,1],[0,0,1]],          
                [[1,0,0],[1,1,1],[0,1,0]],          
                [[0,1,0],[1,1,1],[0,1,0]]        
            ]


