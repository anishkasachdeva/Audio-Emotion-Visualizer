# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m

    
@function
def mirattackslope(orig=None,varargin=None,*args,**kwargs):
    varargin = mirattackslope.varargin
    nargin = mirattackslope.nargin

    #   a = mirattackslope(x) estimates the average slope of each note attack.
#       Values are expressed in the same scale than the original signal,
#       but normalised by time in seconds.
#   Optional arguments:
#   a = mirattackslope(x,m) specifies a method for slope computation.
#       Possible values:
#           m = 'Diff': ratio between the magnitude difference at the 
#               beginning and the ending of the attack period, and the
#               corresponding time difference.
#           m = 'Gauss': average of the slope, weighted by a gaussian
#               curve that emphasizes values at the middle of the attack
#               period. (similar to Peeters 2004).
#   mirattackslope(...,'Contrast',c) specifies the 'Contrast' parameter
#       used in mironsets for event detection through peak picking.
#       Same default value as in mironsets.
#   mirattackslope(...,'Single') only selects one attack phase in the
#       signal (or in each segment).
    
    # Peeters. G. (2004). A large set of audio features for sound description
# (similarity and classification) in the CUIDADO project. version 1.0
    
    meth.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:23
    meth.choice = copy(cellarray(['Diff','Gauss']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:24
    meth.default = copy('Diff')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:25
    option.meth = copy(meth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:26
    cthr.key = copy('Contrast')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:28
    cthr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:29
    cthr.default = copy(NaN)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:30
    option.cthr = copy(cthr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:31
    single.key = copy('Single')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:33
    single.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:34
    single.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:35
    option.single = copy(single)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:36
    log.key = copy(cellarray(['LogOnset','LogCurve']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:38
    log.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:39
    log.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:40
    option.log = copy(log)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:41
    minlog.key = copy('MinLog')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:43
    minlog.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:44
    minlog.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:45
    option.minlog = copy(minlog)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:46
    envmeth.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:48
    envmeth.choice = copy(cellarray(['Filter','Spectro']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:49
    envmeth.default = copy('Spectro')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:50
    option.envmeth = copy(envmeth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:51
    presilence.key = copy('PreSilence')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:53
    presilence.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:54
    presilence.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:55
    option.presilence = copy(presilence)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:56
    postsilence.key = copy('PostSilence')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:58
    postsilence.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:59
    postsilence.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:60
    option.postsilence = copy(postsilence)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:61
    attack.key = copy(cellarray(['Attack','Attacks']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:63
    attack.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:64
    attack.choice = copy(cellarray(['Derivate','Effort']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:65
    attack.default = copy('Derivate')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:66
    option.attack = copy(attack)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:67
    normal.key = copy('Normal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:69
    normal.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:70
    normal.choice = copy(cellarray([0,1,'AcrossSegments']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:71
    normal.default = copy('AcrossSegments')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:72
    option.normal = copy(normal)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:73
    envmeth.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:75
    envmeth.choice = copy(cellarray(['Filter','Spectro']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:76
    envmeth.default = copy('Spectro')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:77
    option.envmeth = copy(envmeth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:78
    ds.key = copy(cellarray(['Down','PostDecim']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:80
    ds.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:81
    if isamir(orig,'mirenvelope'):
        ds.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:83
    else:
        ds.default = copy(NaN)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:85
    
    option.ds = copy(ds)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:87
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:89
    varargout=mirfunction(mirattackslope,orig,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:91
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if isnan(option.ds):
        if strcmpi(option.envmeth,'Spectro'):
            option.ds = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:97
        else:
            option.ds = copy(16)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:99
    
    o=mironsets(x,option.envmeth,'Attack',option.attack,'Down',option.ds,'Contrast',option.cthr,'Single',option.single,'Log',option.log,'MinLog',option.minlog,'Presilence',option.presilence,'PostSilence',option.postsilence,'Normal',option.normal)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:102
    type_=mirtype(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:107
    
@function
def main(o=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(o):
        o=o[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:112
    
    ap=get(o,'AttackPos')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:114
    op=get(o,'OnsetPos')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:115
    apu=get(o,'AttackPosUnit')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:116
    opu=get(o,'OnsetPosUnit')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:117
    sr=get(o,'Sampling')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:118
    d=get(o,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:119
    sl=mircompute(algo,op,ap,opu,apu,d,option.meth,sr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:120
    fp=mircompute(frampose,opu,apu)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:121
    sl=mirscalar(o,'Data',sl,'FramePos',fp,'Title','Attack Slope')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:122
    sl=cellarray([sl,o])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:123
    
@function
def frampose(op=None,ap=None,*args,**kwargs):
    varargin = frampose.varargin
    nargin = frampose.nargin

    if isempty(op):
        fp=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:128
        return fp
    
    op=sort(op[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:131
    ap=sort(ap[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:132
    if length(op) > length(ap):
        op[arange(length(ap) + 1,end())]=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:134
    
    fp=concat([[ravel(op).T],[ravel(ap).T]])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:136
    
@function
def algo(po=None,pa=None,pou=None,pau=None,d=None,meth=None,sr=None,*args,**kwargs):
    varargin = algo.varargin
    nargin = algo.nargin

    if isempty(pa):
        sl=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:141
        return sl
    
    pa=sort(pa[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:144
    po=sort(po[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:145
    pau=sort(pau[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:146
    pou=sort(pou[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:147
    sl=zeros(1,length(pa))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:148
    for i in arange(1,length(pa)).reshape(-1):
        if 'Diff' == meth:
            sl[i]=(d(pa(i)) - d(po(i))) / (pau(i) - pou(i))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:152
        else:
            if 'Gauss' == meth:
                l=pa(i) - po(i)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:154
                h=ceil(l / 2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:155
                gauss=exp(- (arange(1 - h,l - h)) ** 2 / (l / 4) ** 2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:156
                dat=multiply(diff(d(arange(po(i),pa(i)))),gauss.T)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:157
                sl[i]=dot(mean(dat),sr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattackslope.m:158
    