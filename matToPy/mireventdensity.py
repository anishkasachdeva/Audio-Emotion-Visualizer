# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m

    
@function
def mireventdensity(x=None,varargin=None,*args,**kwargs):
    varargin = mireventdensity.varargin
    nargin = mireventdensity.nargin

    #   e = mireventdensity(x) estimate the mean frequency of events (i.e., how
#       many note onsets per second) in the temporal data x.
    
    #   Optional arguments: Option1, Option2
# Tuomas Eerola, 14.08.2008
    
    normal.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:8
    normal.choice = copy(cellarray(['Option1','Option2']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:9
    normal.default = copy('Option1')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:10
    option.normal = copy(normal)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:11
    frame.key = copy('Frame')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:13
    frame.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:14
    frame.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:15
    frame.default = copy(concat([0,0]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:16
    frame.keydefault = copy(concat([10,1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:17
    option.frame = copy(frame)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:18
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:20
    #specif.eachchunk = 'Normal';
    specif.combinechunk = copy(cellarray(['Average','Concat']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:23
    specif.nochunk = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:25
    varargout=mirfunction(mireventdensity,x,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:27
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if isamir(x,'mirenvelope'):
        if logical_not(isframed(x)) and option.frame.length.val:
            x=mirframe(x,option.frame.length.val,option.frame.length.unit,option.frame.hop.val,option.frame.hop.unit,option.frame.phase.val,option.frame.phase.unit,option.frame.phase.atend)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:33
    else:
        if option.frame.length.val:
            x=mironsets(x,'Frame',option.frame.length.val,option.frame.length.unit,option.frame.hop.val,option.frame.hop.unit,option.frame.phase.val,option.frame.phase.unit,option.frame.phase.atend)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:43
        else:
            x=mironsets(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:51
    
    type_='mirscalar'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:54
    
@function
def main(o=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(o):
        o=o[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:59
    
    sr=get(o,'Sampling')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:61
    p=mirpeaks(o)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:63
    
    # And what is peaks already computed? p = o?
    
    pv=get(p,'PeakVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:66
    v=mircompute(algo,pv,o,option,sr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:67
    e=mirscalar(o,'Data',v,'Title','Event density','Unit','per second')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:68
    e=cellarray([e,o])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:69
    
@function
def algo(pv=None,o=None,option=None,sr=None,*args,**kwargs):
    varargin = algo.varargin
    nargin = algo.nargin

    nc=size(o,2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:73
    nch=size(o,3)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:74
    e=zeros(1,nc,nch)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:75
    # for i = 1:nch
#     for j = 1:nc
#         if option.root
#             e(1,j,i) = norm(d(:,j,i));
#         else
#             disp('do the calc...')
#  #           e(1,j,i) = d(:,j,i)'*d(:,j,i);
#             #tmp = mironsets(d,'Filterbank',10,'Contrast',0.1); # Change by TE, was only FB=20, no other params
#             e2 = mirpeaks(e)
#             [o1,o2] = mirgetdata(e);
#             e(1,j,i) = length(o2)/mirgetdata(mirlength(d)); 
#         end
#     end
# end
    for i in arange(1,nch).reshape(-1):
        for j in arange(1,nc).reshape(-1):
            e[1,j,i]=length(pv[1,j,i])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:92
            if strcmpi(option.normal,'Option1'):
                e[1,j,i]=dot(e(1,j,i),sr) / size(o,1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:94
            else:
                if strcmpi(option.normal,'Option2'):
                    pvs=pv[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:96
                    high_pvs=length(find(mean(pvs) > pvs))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:97
                    e[1,j,i]=dot(high_pvs(1,j,i),sr) / size(o,1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mireventdensity.m:98
    
    #function [y orig] = eachchunk(orig,option,missing,postchunk)
#y = mireventdensity(orig,option);
    
    #function y = combinechunk(old,new)
#do = mirgetdata(old);
#dn = mirgetdata(new);
#y = set(old,'ChunkData',do+dn);