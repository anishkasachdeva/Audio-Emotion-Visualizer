# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m

    
@function
def mirspread(orig=None,varargin=None,*args,**kwargs):
    varargin = mirspread.varargin
    nargin = mirspread.nargin

    #   S = mirspread(x) calculates the spread of x, which can be either:
#       - a spectrum (spectral spread),
#       - an envelope (temporal spread), or
#       - any histogram.
    
    minrms.key = copy('MinRMS')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:7
    minrms.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:8
    minrms.type = copy('Numerical')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:9
    minrms.default = copy(0.01)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:10
    option.minrms = copy(minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:11
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:13
    varargout=mirfunction(mirspread,orig,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:15
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if not_(isamir(x,'mirdata')) or isamir(x,'miraudio'):
        x=mirspectrum(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:20
    
    type_='mirscalar'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:22
    
@function
def main(x=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(x):
        x=x[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:27
    
    y=peaksegments(spread,get(x,'Data'),get(x,'Pos'),get(mircentroid(x,'MaxEntropy',0),'Data'))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:29
    if isa(x,'mirspectrum'):
        t='Spectral spread'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:33
    else:
        if isa(x,'mirenvelope'):
            t='Temporal spread'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:35
        else:
            t=concat(['Spread of ',get(x,'Title')])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:37
    
    S=mirscalar(x,'Data',y,'Title',t)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:39
    if isstruct(postoption) and strcmpi(get(x,'Title'),'Spectrum') and isfield(postoption,'minrms') and postoption.minrms:
        S=after(x,S,postoption.minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:42
    
    
@function
def spread(d=None,p=None,c=None,*args,**kwargs):
    varargin = spread.varargin
    nargin = spread.nargin

    s=sqrt(sum(multiply((p - c) ** 2,(d / sum(d)))))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:47
    
@function
def after(x=None,S=None,minrms=None,*args,**kwargs):
    varargin = after.varargin
    nargin = after.nargin

    r=mirrms(x,'Warning',0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:51
    v=mircompute(trim,get(S,'Data'),get(r,'Data'),minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:52
    S=set(S,'Data',v)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:53
    
@function
def trim(d=None,r=None,minrms=None,*args,**kwargs):
    varargin = trim.varargin
    nargin = trim.nargin

    r=r / max(max(r))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:57
    pos=find(r < minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:58
    for i in arange(1,length(pos)).reshape(-1):
        d[pos(i)]=NaN
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:60
    
    d=cellarray([d])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirspread.m:62