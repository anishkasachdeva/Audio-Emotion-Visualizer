# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m

    
@function
def mirrms(x=None,varargin=None,*args,**kwargs):
    varargin = mirrms.varargin
    nargin = mirrms.nargin

    #   e = mirrms(x) calculates the root mean square energy.
#   Optional arguments:
#       mirrms(...,'Frame') computes the temporal evolution of the energy.
    
    notchunking.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:6
    notchunking.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:7
    notchunking.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:8
    option.notchunking = copy(notchunking)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:9
    median.key = copy('Median')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:11
    median.when = copy('Both')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:12
    median.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:13
    median.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:14
    option.median = copy(median)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:15
    warning.key = copy('Warning')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:17
    warning.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:18
    warning.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:19
    option.warning = copy(warning)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:20
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:22
    specif.defaultframelength = copy(0.05)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:24
    specif.defaultframehop = copy(0.5)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:25
    specif.combinechunk = copy('Sum')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:27
    varargout=mirfunction(mirrms,x,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:29
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    type_='mirscalar'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:33
    
@function
def main(x=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(x):
        x=x[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:38
    
    if logical_not(isamir(x,'mirscalar')):
        if option.warning and logical_not(isamir(x,'miraudio')):
            warning(concat(['Do you really intend to apply MIRRMS on a ',class_(x),'?']))
        d=get(x,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:44
        v=mircompute(algo,d,option.median)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:45
        x=mirscalar(x,'Data',v,'Title','RMS energy')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:46
    
    if isstruct(postoption) and isfield(postoption,'notchunking') and postoption.notchunking:
        if logical_not(postoption.median):
            x=after(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:51
    else:
        if option.median:
            mirerror('MIRRMS',''Median' option should not be used in chunk decomposition mode. Results will not be reliable. Try mirchunklim(Inf)')
    
    
@function
def algo(d=None,option_median=None,*args,**kwargs):
    varargin = algo.varargin
    nargin = algo.nargin

    nc=size(d,2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:59
    nch=size(d,3)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:60
    e=zeros(1,nc,nch)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:61
    if option_median:
        for i in arange(1,nch).reshape(-1):
            for j in arange(1,nc).reshape(-1):
                e[1,j,i]=sqrt(median(d(arange(),j,i) ** 2))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:65
    else:
        for i in arange(1,nch).reshape(-1):
            for j in arange(1,nc).reshape(-1):
                e[1,j,i]=dot(d(arange(),j,i).T,d(arange(),j,i))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:71
    
    
@function
def after(x=None,*args,**kwargs):
    varargin = after.varargin
    nargin = after.nargin

    v=mircompute(afternorm,get(x,'Data'),get(x,'Length'))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:78
    x=set(x,'Data',v)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:79
    
@function
def afternorm(d=None,l=None,*args,**kwargs):
    varargin = afternorm.varargin
    nargin = afternorm.nargin

    d=sqrt(d / l)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirrms.m:83