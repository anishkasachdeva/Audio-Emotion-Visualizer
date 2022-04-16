# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m

    
@function
def mirattacktime(orig=None,varargin=None,*args,**kwargs):
    varargin = mirattacktime.varargin
    nargin = mirattacktime.nargin

    #   a = mirattacktime(x) returns the duration (in s.) of each note attack. 
#   Optional arguments:
#   a = mirattacktime(x,l) specifies whether to consider the duration in s.
#       (l='Lin') or the logarithm of that duration (l='Log') following the
#       approach proposed in Krimphoff et al. (1994).
#       Default value: l='Lin'.
#   mirattacktime(...,'Single') only selects one attack phase in the signal
#       (or in each segment).
    
    # Krimphoff, J., McAdams, S. & Winsberg, S. (1994), Caract?risation du 
# timbre des sons complexes. II : Analyses acoustiques et quantification 
# psychophysique. Journal de Physique, 4(C5), 625-628.
    
    scale.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:15
    scale.choice = copy(cellarray(['Lin','Log']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:16
    scale.default = copy('Lin')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:17
    option.scale = copy(scale)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:18
    cthr.key = copy('Contrast')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:20
    cthr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:21
    cthr.default = copy(NaN)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:22
    option.cthr = copy(cthr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:23
    single.key = copy('Single')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:25
    single.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:26
    single.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:27
    option.single = copy(single)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:28
    log.key = copy(cellarray(['LogOnset','LogCurve']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:30
    log.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:31
    log.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:32
    option.log = copy(log)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:33
    minlog.key = copy('MinLog')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:35
    minlog.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:36
    minlog.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:37
    option.minlog = copy(minlog)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:38
    presilence.key = copy('PreSilence')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:40
    presilence.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:41
    presilence.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:42
    option.presilence = copy(presilence)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:43
    postsilence.key = copy('PostSilence')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:45
    postsilence.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:46
    postsilence.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:47
    option.postsilence = copy(postsilence)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:48
    attack.key = copy(cellarray(['Attack','Attacks']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:50
    attack.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:51
    attack.choice = copy(cellarray(['Derivate','Effort']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:52
    attack.default = copy('Derivate')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:53
    option.attack = copy(attack)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:54
    envmeth.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:56
    envmeth.choice = copy(cellarray(['Filter','Spectro']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:57
    envmeth.default = copy('Spectro')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:58
    option.envmeth = copy(envmeth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:59
    ds.key = copy(cellarray(['Down','PostDecim']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:61
    ds.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:62
    if isamir(orig,'mirenvelope'):
        ds.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:64
    else:
        ds.default = copy(NaN)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:66
    
    option.ds = copy(ds)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:68
    cutoff.key = copy('CutOff')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:70
    cutoff.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:71
    cutoff.default = copy(37)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:72
    option.cutoff = copy(cutoff)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:73
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:75
    varargout=mirfunction(mirattacktime,orig,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:77
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if isnan(option.ds):
        if strcmpi(option.envmeth,'Spectro'):
            option.ds = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:83
        else:
            option.ds = copy(16)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:85
    
    o=mironsets(x,option.envmeth,'Attack',option.attack,'Down',option.ds,'Contrast',option.cthr,'Single',option.single,'Log',option.log,'MinLog',option.minlog,'Presilence',option.presilence,'PostSilence',option.postsilence,'Normal','AcrossSegments','CutOff',option.cutoff)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:88
    type_=mirtype(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:93
    
@function
def main(o=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(o):
        o=o[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:98
    
    ap=get(o,'AttackPosUnit')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:100
    op=get(o,'OnsetPosUnit')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:101
    at=mircompute(algo,op,ap,option.scale)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:102
    fp=mircompute(frampose,op,ap)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:103
    if strcmpi(option.scale,'Lin'):
        unit='s.'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:105
    else:
        unit=''
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:107
    
    at=mirscalar(o,'Data',at,'FramePos',fp,'Title','Attack Time','Unit',unit)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:109
    at=cellarray([at,o])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:110
    
@function
def frampose(op=None,ap=None,*args,**kwargs):
    varargin = frampose.varargin
    nargin = frampose.nargin

    if isempty(op):
        fp=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:115
        return fp
    
    op=sort(op[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:118
    ap=sort(ap[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:119
    if length(op) > length(ap):
        op[arange(length(ap) + 1,end())]=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:121
    
    fp=concat([[ravel(op).T],[ravel(ap).T]])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:123
    
@function
def algo(op=None,ap=None,sc=None,*args,**kwargs):
    varargin = algo.varargin
    nargin = algo.nargin

    if isempty(ap):
        at=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:128
        return at
    
    op=sort(op[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:131
    ap=sort(ap[1])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:132
    if length(op) > length(ap):
        op[arange(length(ap) + 1,end())]=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:134
    
    at=ap - op
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:136
    at=at.T
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:137
    if strcmpi(sc,'Log'):
        at=log10(at)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:139
    
    at=at.T
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirattacktime.m:141