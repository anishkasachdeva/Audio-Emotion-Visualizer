# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m

    
@function
def mirfluctuation(orig=None,varargin=None,*args,**kwargs):
    varargin = mirfluctuation.varargin
    nargin = mirfluctuation.nargin

    #   f = mirfluctuation(x) calculates the fluctuation strength, indicating
#       the rhythmic periodicities along the different channels.
#   Optional arguments:
#       mirfluctuation(...,'MinRes',mr) specifies the minimal frequency
#           resolution of the resulting spectral decomposition, in Hz.
#               Default: mr = .01 Hz
#       mirfluctuation(...,'Summary') returns the summary of the
#           fluctuation, i.e., the summation along the critical bands.
#       mirfluctuation(..., 'InnerFrame', l, r) specifies the spectrogram 
#           frame length l (in second), and, optionally, the frame rate r 
#           (in Hertz), with by default a frame length of 23 ms and a frame
#           rate of 80 Hz.
#       mirfluctuation(..., 'Frame', l, r) computes fluctuation using a 
#           window moving along the spectrogram, whose length l (in second)
#           and frame rate r (in Hertz) can be specified as well, with by
#           default a frame length of 1 s and a frame rate of 10 Hz.
    
    # E. Pampalk, A. Rauber, D. Merkl, "Content-based Organization and 
# Visualization of Music Archives",
    
    sum.key = copy('Summary')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:22
    sum.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:23
    sum.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:24
    option.sum = copy(sum)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:25
    mr.key = copy('MinRes')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:27
    mr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:28
    mr.default = copy(0.01)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:29
    option.mr = copy(mr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:30
    max.key = copy('Max')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:32
    max.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:33
    max.default = copy(10)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:34
    option.max = copy(max)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:35
    band.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:37
    band.choice = copy(cellarray(['Mel','Bark']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:38
    band.default = copy('Bark')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:39
    option.band = copy(band)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:40
    inframe.key = copy('InnerFrame')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:42
    inframe.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:43
    inframe.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:44
    inframe.default = copy(concat([0.023,80]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:45
    option.inframe = copy(inframe)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:46
    frame.key = copy('Frame')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:48
    frame.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:49
    frame.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:50
    frame.default = copy(concat([0,0]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:51
    frame.keydefault = copy(concat([1,10]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:52
    option.frame = copy(frame)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:53
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:55
    specif.nochunk = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:56
    varargout=mirfunction(mirfluctuation,orig,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:58
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if iscell(x):
        x=x[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:63
    
    if option.inframe(2) < dot(option.max,2):
        option.inframe[2]=dot(option.max,2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:66
    
    if isamir(x,'miraudio') and not_(isframed(x)):
        x=mirframe(x,option.inframe(1),'s',option.inframe(2),'Hz')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:69
    
    s=mirspectrum(x,'Power','Terhardt',option.band,'dB','Mask')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:71
    type_='mirspectrum'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:72
    
@function
def main(x=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    d=get(x,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:76
    fp=get(x,'FramePos')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:77
    fl=option.frame.length.val
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:78
    fh=option.frame.hop.val
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:79
    if logical_not(fl):
        f=mirspectrum(x,'AlongBands','Max',option.max,'Window',0,'NormalLength','Resonance','Fluctuation','MinRes',option.mr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:81
    else:
        vb=copy(mirverbose)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:85
        mirverbose(0)
        df=cell(1,length(d))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:88
        fp2=cell(1,length(d))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:89
        p2=cell(1,length(d))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:90
        for i in arange(1,length(d)).reshape(-1):
            df[i]=cell(1,length(d[i]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:92
            fp2[i]=cell(1,length(d[i]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:93
            for j in arange(1,length(d[i])).reshape(-1):
                dur=fp[i][j](1,end()) - fp[i][j](1,1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:95
                srj=size(d[i][j],2) / dur
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:96
                flj=round(dot(fl,srj))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:97
                fhj=srj / fh
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:99
                n=floor(dot((dur - fl),fh)) + 1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:100
                fp2[i][j]=zeros(2,n)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:101
                for k in arange(1,n).reshape(-1):
                    st=round(dot((k - 1),fhj)) + 1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:103
                    stend=st + flj - 1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:104
                    dk=d[i][j](arange(),arange(st,stend),arange())
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:105
                    fpk=fp[i][j](arange(),arange(st,stend))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:106
                    x2=set(x,'Data',cellarray([cellarray([dk])]),'FramePos',cellarray([cellarray([fpk])]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:107
                    fk=mirspectrum(x2,'AlongBands','Max',10,'Window',0,'NormalLength','Resonance','Fluctuation','MinRes',option.mr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:108
                    dfk=mirgetdata(fk)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:112
                    if k == 1:
                        df[i][j]=zeros(size(dfk,1),n,size(dfk,3))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:114
                    df[i][j][arange(),k,arange()]=dfk
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:116
                    fp2[i][j][arange(),k]=concat([[fpk(1)],[fpk(end())]])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:117
                p=get(fk,'Pos')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:119
                p2[i][j]=repmat(p[1][1],concat([1,n,1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:120
        f=set(fk,'Data',df,'FramePos',fp2,'Pos',p2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:123
        mirverbose(vb)
    
    if option.sum:
        f=mirsummary(f)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:129
    
    f=set(f,'Title','Fluctuation')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirfluctuation.m:131