# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m

    
@function
def mirkey(orig=None,varargin=None,*args,**kwargs):
    varargin = mirkey.varargin
    nargin = mirkey.nargin

    #   k = mirkey(x) estimates the key.
#   Optional argument:
#       mirkey(...,'Total',m) selects not only the most probable key, but
#           the m most probable keys.
#       The other parameter 'Contrast' related to mirpeaks can be specified 
#           here (see help mirchromagram).
#       The optional parameters 'Weight' and 'Triangle' related to
#           mirchromagram can be specified here (see help mirchromagram).
#   [k,ks] = mirkey(...) also returns the key clarity, corresponding here 
#       to the key strength associated to the best candidate.
#   [k,ks,ksc] = mirkey(...) also displays the key strength curve used for
#       the key estimation and shows in particular the peaks corresponding 
#       to the selected key(s).
    
    tot.key = copy('Total')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:16
    tot.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:17
    tot.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:18
    option.tot = copy(tot)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:19
    thr.key = copy('Contrast')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:21
    thr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:22
    thr.default = copy(0.1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:23
    option.thr = copy(thr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:24
    wth.key = copy('Weight')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:26
    wth.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:27
    wth.default = copy(0.5)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:28
    option.wth = copy(wth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:29
    tri.key = copy('Triangle')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:31
    tri.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:32
    tri.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:33
    option.tri = copy(tri)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:34
    meth.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:36
    meth.choice = copy(cellarray(['Gomez','Lartillot','Gomez+']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:37
    meth.default = copy('Gomez')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:38
    option.meth = copy(meth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:39
    origin.key = copy('Tuning')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:41
    origin.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:42
    origin.default = copy(261.6256)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:43
    option.origin = copy(origin)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:44
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:46
    specif.defaultframelength = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:47
    specif.defaultframehop = copy(0.5)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:48
    varargout=mirfunction(mirkey,orig,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:50
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if not_(isamir(x,'mirkeystrength')):
        x=mirkeystrength(x,'Weight',option.wth,'Triangle',option.tri,option.meth,'Tuning',option.origin)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:55
    
    p=mirpeaks(x,'Total',option.tot,'Contrast',option.thr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:59
    type_=cellarray(['mirscalar','mirscalar','mirkeystrength'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:60
    
@function
def main(p=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(p):
        p=p[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:65
    
    pc=get(p,'PeakPos')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:67
    pv=get(p,'PeakMaxVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:68
    pm=get(p,'PeakMode')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:69
    k=mirscalar(p,'Data',pc,'Mode',pm,'Title','Key','Legend',cellarray(['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:70
    m=mirscalar(p,'Data',pv,'Title','Key clarity','MultiData',cellarray([]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:72
    k=cellarray([k,m,p])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirkey.m:73