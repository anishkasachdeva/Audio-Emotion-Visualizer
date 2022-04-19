# Generated with SMOP  0.41-beta
# from libsmop import *
from smop.libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m

    
@function
def mirlowenergy(x=None,varargin=None,*args,**kwargs):
    varargin = mirlowenergy.varargin
    nargin = mirlowenergy.nargin

    #   p = mirlowenergy(f) computes the percentage of frames showing a RMS 
#       energy that is lower than a given threshold. 
#   For instance, for a musical excerpt with some very loud frames and 
#       lots of silent frames, we would get a high low-energy rate.
#   Optional argument:
#       mirlowenergy(...,'Threshold',t) expressed as a ratio to the average
#           energy over the frames.
#           Default value: t = 1
#       mirlowenergy(...,'Frame',l,h) specifies the use of frames of
#           length l seconds and a hop rate h.
#           Default values: l = .05 s, h = .5
#       mirlowenergy(...,'Root',0) uses mean square instead of root mean
#           square
#       mirlowenergy(...,'ASR') computes the Average Silence Ratio, which
#       corresponds in fact to a RMS without the square-root, and a default
#       threshold set to t = .5
#   [p,e] = mirlowenergy(...) also returns the RMS energy curve.
    
    asr.key = copy('ASR')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:20
    asr.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:21
    asr.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:22
    option.asr = copy(asr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:23
    thr.key = copy('Threshold')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:25
    thr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:26
    thr.default = copy(NaN)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:27
    option.thr = copy(thr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:28
    frame.key = copy('Frame')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:30
    frame.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:31
    frame.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:32
    frame.default = copy(concat([0.05,0.5]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:33
    option.frame = copy(frame)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:34
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:36
    specif.combinechunk = copy(cellarray(['Average',nothing]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:38
    specif.extensive = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:39
    varargout=mirfunction(mirlowenergy,x,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:41
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if isamir(x,'miraudio'):
        if isframed(x):
            x=mirrms(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:47
        else:
            x=mirrms(x,'Frame',option.frame.length.val,option.frame.length.unit,option.frame.hop.val,option.frame.hop.unit,option.frame.phase.val,option.frame.phase.unit,option.frame.phase.atend)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:49
    
    type_='mirscalar'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:55
    
@function
def main(r=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(r):
        r=r[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:60
    
    if isnan(option.thr):
        if option.asr:
            option.thr = copy(0.5)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:64
        else:
            option.thr = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:66
    
    v=mircompute(algo,get(r,'Data'),option.thr,option.asr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:69
    fp=mircompute(noframe,get(r,'FramePos'))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:70
    e=mirscalar(r,'Data',v,'Title','Low energy','Unit','/1','FramePos',fp)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:71
    e=cellarray([e,r])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:72
    
@function
def algo(d=None,thr=None,asr=None,*args,**kwargs):
    varargin = algo.varargin
    nargin = algo.nargin

    if asr:
        d=d ** 2
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:77
    
    v=sum(d < repmat(dot(thr,mean(d,2)),concat([1,size(d,2),1])))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:79
    v=v / size(d,2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:80
    
@function
def noframe(fp=None,*args,**kwargs):
    varargin = noframe.varargin
    nargin = noframe.nargin

    fp=concat([[fp(1)],[fp(end())]])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:84
    
@function
def nothing(old=None,new=None,*args,**kwargs):
    varargin = nothing.varargin
    nargin = nothing.nargin

    y=copy(old)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirlowenergy.m:88