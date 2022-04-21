# Generated with SMOP  0.41-beta
from libsmop import *
# miraudio.m

    
@function
def miraudio(orig=None,varargin=None,*args,**kwargs):
    varargin = miraudio.varargin
    nargin = miraudio.nargin

    #   a = miraudio('filename') loads the sound file 'filename' (in WAV or AU
#       format) into a miraudio object.
#   a = miraudio('Folder') loads all the sound files in the CURRENT folder
#       into a miraudio object.
#   a = miraudio(v,sr), where v is a column vector, translates the vector v
#       into a miraudio object. The sampling frequency is set to sr Hertz.
#           Default value for sr: 44100 Hz.
#   a = miraudio(b, ...), where b is already a miraudio object, performs 
#       operations on b specified by the optional arguments (see below).
    
    #   Transformation options:
#       miraudio(...,'Mono',0) does not perform the default summing of
#           channels into one single mono track, but instead stores each 
#           channel of the initial soundfile separately.       
#       miraudio(...,'Center') centers the signals.
#       miraudio(...,'Sampling',r) resamples at sampling rate r (in Hz).
#           (Requires the Signal Processing Toolbox.)
#       miraudio(...,'Normal') normalizes with respect to RMS energy.
#   Extraction options:
#       miraudio(...,'Extract',t1,t2,u,f) extracts the signal between dates
#           t1 and t2, expressed in the unit u.
#           Possible values for u:
#               's' (seconds, by default),
#               'sp' (sample index, starting from 1).
#           The additional optional argument f indicates the referential
#               origin of the temporal positions. Possible values for f:
#               'Start' (by default)
#               'Middle' (of the sequence)
#               'End' of the sequence
#               When using 'Middle' or 'End', negative values for t1 or t2
#               indicate values before the middle or the end of the audio
#               sequence.
#       miraudio(...,'Trim') trims the pseudo-silence beginning and end off
#           the audio file. Silent frames are frames with RMS below t times
#           the medium RMS of the whole audio file.
#               Default value: t = 0.06
#           instead of 'Trim':
#              'TrimStart' only trims the beginning of the audio file,
#              'TrimEnd' only trims the end.
#           miraudio(...,'TrimThreshold',t) specifies the trimming threshold t.
#       miraudio(...,'Channel',c) or miraudio(...,'Channels',c) selects the
#           channels indicated by the (array of) integer(s) c.
#   Labeling option:
#       miraudio(...,'Label',l) labels the audio signal(s) following the 
#           label(s) l.
#           If l is a (series of) number(s), the audio signal(s) are
#           labelled using the substring of their respective file name of 
#           index l. If l=0, the audio signal(s) are labelled using the
#           whole file name.
    
    if isempty(orig):
        varargout=cellarray([cellarray([])])
# miraudio.m:54
        return varargout
    
    if isnumeric(orig):
        if size(orig,2) > 1 or size(orig,3) > 1:
            mirerror('MIRAUDIO','Only column vectors can be imported into mirtoolbox.')
        if nargin == 1:
            f=44100
# miraudio.m:63
        else:
            f=varargin[1]
# miraudio.m:65
        b=32
# miraudio.m:67
        if size(orig,1) == 1:
            orig=orig.T
# miraudio.m:69
        tp=(arange(0,size(orig,1) - 1)).T / f
# miraudio.m:71
        l=(size(orig,1) - 1)
# miraudio.m:72
        t=mirtemporal([],'Time',cellarray([cellarray([tp])]),'Data',cellarray([cellarray([orig])]),'Length',cellarray([cellarray([l])]),'FramePos',cellarray([cellarray([tp(concat([1,end()]))])]),'Sampling',cellarray([f]),'Name',cellarray([inputname(1)]),'Label',cellarray([cellarray([])]),'Clusters',cellarray([cellarray([])]),'Channels',[],'Centered',0,'NBits',cellarray([b]),'Title','Audio signal','PeakPos',cellarray([cellarray([cellarray([])])]),'PeakVal',cellarray([cellarray([cellarray([])])]),'PeakMode',cellarray([cellarray([cellarray([])])]))
# miraudio.m:73
        aa.fresh = copy(1)
# miraudio.m:79
        aa.extracted = copy(0)
# miraudio.m:80
        varargout=cellarray([class_(aa,'miraudio',t)])
# miraudio.m:81
        return varargout
    
    center.key = copy('Center')
# miraudio.m:86
    center.type = copy('Boolean')
# miraudio.m:87
    center.default = copy(0)
# miraudio.m:88
    center.when = copy('After')
# miraudio.m:89
    option.center = copy(center)
# miraudio.m:90
    normal.key = copy('Normal')
# miraudio.m:92
    normal.type = copy('String')
# miraudio.m:93
    normal.choice = copy(cellarray(['RMS','Max']))
# miraudio.m:94
    normal.default = copy(0)
# miraudio.m:95
    normal.keydefault = copy('RMS')
# miraudio.m:96
    normal.when = copy('After')
# miraudio.m:97
    option.normal = copy(normal)
# miraudio.m:98
    extract.key = copy(cellarray(['Extract','Excerpt']))
# miraudio.m:100
    extract.type = copy('Integer')
# miraudio.m:101
    extract.number = copy(2)
# miraudio.m:102
    extract.default = copy([])
# miraudio.m:103
    extract.unit = copy(cellarray(['s','sp']))
# miraudio.m:104
    extract.defaultunit = copy('s')
# miraudio.m:105
    extract.from = copy(cellarray(['Start','Middle','End']))
# miraudio.m:106
    extract.defaultfrom = copy('Start')
# miraudio.m:107
    option.extract = copy(extract)
# miraudio.m:108
    trim.type = copy('String')
# miraudio.m:110
    trim.choice = copy(cellarray(['NoTrim','Trim','TrimBegin','TrimStart','TrimEnd']))
# miraudio.m:111
    trim.default = copy('NoTrim')
# miraudio.m:112
    trim.when = copy('After')
# miraudio.m:113
    option.trim = copy(trim)
# miraudio.m:114
    trimthreshold.key = copy('TrimThreshold')
# miraudio.m:116
    trimthreshold.type = copy('Integer')
# miraudio.m:117
    trimthreshold.default = copy(0.06)
# miraudio.m:118
    trimthreshold.when = copy('After')
# miraudio.m:119
    option.trimthreshold = copy(trimthreshold)
# miraudio.m:120
    smoothborder.key = copy('SmoothBorder')
# miraudio.m:122
    smoothborder.type = copy('Integer')
# miraudio.m:123
    smoothborder.default = copy(0)
# miraudio.m:124
    smoothborder.keydefault = copy(1)
# miraudio.m:125
    smoothborder.when = copy('After')
# miraudio.m:126
    option.smoothborder = copy(smoothborder)
# miraudio.m:127
    label.key = copy('Label')
# miraudio.m:129
    label.default = copy('')
# miraudio.m:130
    label.when = copy('After')
# miraudio.m:131
    option.label = copy(label)
# miraudio.m:132
    sampling.key = copy('Sampling')
# miraudio.m:134
    sampling.type = copy('Integer')
# miraudio.m:135
    sampling.default = copy(0)
# miraudio.m:136
    sampling.when = copy('Both')
# miraudio.m:137
    option.sampling = copy(sampling)
# miraudio.m:138
    
    #     segment.type = 'Integer';
   #     segment.default = [];
   #     segment.when = 'After';
   # option.segment = segment;
    
    mono.key = copy('Mono')
# miraudio.m:146
    mono.type = copy('Boolean')
# miraudio.m:147
    mono.default = copy(NaN)
# miraudio.m:148
    mono.when = copy('After')
# miraudio.m:149
    option.mono = copy(mono)
# miraudio.m:150
    fwr.key = copy('FWR')
# miraudio.m:152
    fwr.type = copy('Boolean')
# miraudio.m:153
    fwr.default = copy(0)
# miraudio.m:154
    fwr.when = copy('After')
# miraudio.m:155
    option.fwr = copy(fwr)
# miraudio.m:156
    separate.key = copy('SeparateChannels')
# miraudio.m:158
    separate.type = copy('Boolean')
# miraudio.m:159
    separate.default = copy(0)
# miraudio.m:160
    option.separate = copy(separate)
# miraudio.m:161
    Ch.key = copy(cellarray(['Channel','Channels']))
# miraudio.m:163
    Ch.type = copy('Integer')
# miraudio.m:164
    Ch.default = copy([])
# miraudio.m:165
    Ch.when = copy('After')
# miraudio.m:166
    option.Ch = copy(Ch)
# miraudio.m:167
    specif.option = copy(option)
# miraudio.m:169
    specif.beforechunk = copy(cellarray([beforechunk,'normal']))
# miraudio.m:171
    specif.eachchunk = copy(eachchunk)
# miraudio.m:172
    specif.combinechunk = copy(combinechunk)
# miraudio.m:173
    if nargin > 1 and ischar(varargin[1]) and strcmp(varargin[1],'Now'):
        if nargin > 2:
            extract=varargin[2]
# miraudio.m:177
        else:
            extract=[]
# miraudio.m:179
        para=[]
# miraudio.m:181
        varargout=cellarray([main(orig,[],para,[],extract)])
# miraudio.m:182
    else:
        varargout=mirfunction(miraudio,orig,varargin,nargout,specif,init,main)
# miraudio.m:184
    
    if isempty(varargout):
        varargout=cellarray([cellarray([])])
# miraudio.m:187
    
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if isa(x,'mirdesign'):
        if option.sampling:
            x=setresampling(x,option.sampling)
# miraudio.m:194
    
    type_='miraudio'
# miraudio.m:197
    
@function
def main(orig=None,option=None,after=None,index=None,extract=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(orig):
        orig=orig[1]
# miraudio.m:202
    
    if ischar(orig):
        if nargin < 5:
            # When is this used?
            extract=[]
# miraudio.m:207
        else:
            presil=extract(3)
# miraudio.m:209
            postsil=extract(4)
# miraudio.m:210
            extract=extract(arange(1,2))
# miraudio.m:211
        d[1],tp[1],fp[1],f[1],l[1],b[1],n[1],ch[1]=mirread(extract(arange(1,2)),orig,1,0,nargout=8)
# miraudio.m:213
        l[1][1]=dot(l[1][1],f[1])
# miraudio.m:214
        if presil:
            d[1][1]=concat([[zeros(2000,1,size(d[1][1],3))],[d[1][1]]])
# miraudio.m:216
            tp1=tp[1][1]
# miraudio.m:217
            tp[1][1]=concat([[tp1(1) - dot((arange(2000,1,- 1)).T,(tp1(2) - tp1(1)))],[tp1]])
# miraudio.m:218
        if postsil:
            d[1][1]=concat([[d[1][1]],[zeros(2000,1,size(d[1][1],3))]])
# miraudio.m:221
            tp1=tp[1][1]
# miraudio.m:222
            tp[1][1]=concat([[tp1],[tp1(end()) + dot((arange(1,2000)).T,(tp1(2) - tp1(1)))]])
# miraudio.m:223
        t=mirtemporal([],'Time',tp,'Data',d,'FramePos',fp,'Sampling',f,'Name',n,'Label',cell(1,length(d)),'Clusters',cell(1,length(d)),'Length',l,'Channels',ch,'Centered',0,'NBits',b)
# miraudio.m:225
        t=set(t,'Title','Audio waveform')
# miraudio.m:229
        a.fresh = copy(1)
# miraudio.m:230
        a.extracted = copy(1)
# miraudio.m:231
        a=class_(a,'miraudio',t)
# miraudio.m:232
    else:
        if not_(isempty(option)) and not_(isempty(option.extract)):
            if not_(isstruct(after)):
                after=copy(struct)
# miraudio.m:236
            after.extract = copy(option.extract)
# miraudio.m:238
        if isa(orig,'miraudio'):
            a=copy(orig)
# miraudio.m:241
        else:
            a.fresh = copy(1)
# miraudio.m:243
            a.extracted = copy(0)
# miraudio.m:244
            a=class_(a,'miraudio',orig)
# miraudio.m:245
    
    if not_(isempty(after)):
        a=post(a,after)
# miraudio.m:249
    
    
@function
def post(a=None,para=None,*args,**kwargs):
    varargin = post.varargin
    nargin = post.nargin

    if a.fresh and isfield(para,'mono'):
        a.fresh = copy(0)
# miraudio.m:255
        if isnan(para.mono):
            para.mono = copy(1)
# miraudio.m:257
    
    if isfield(para,'mono') and para.mono == 1:
        a=mirsum(a,'Mean')
# miraudio.m:261
    
    d=get(a,'Data')
# miraudio.m:263
    t=get(a,'Time')
# miraudio.m:264
    ac=get(a,'AcrossChunks')
# miraudio.m:265
    f=get(a,'Sampling')
# miraudio.m:266
    cl=get(a,'Clusters')
# miraudio.m:267
    for h in arange(1,length(d)).reshape(-1):
        for k in arange(1,length(d[h])).reshape(-1):
            tk=t[h][k]
# miraudio.m:270
            dk=d[h][k]
# miraudio.m:271
            if isfield(para,'extract') and not_(isempty(para.extract)) and logical_not(a.extracted):
                t1=para.extract(1)
# miraudio.m:274
                t2=para.extract(2)
# miraudio.m:275
                if para.extract(4):
                    if para.extract(4) == 1:
                        shift=round(size(tk,1) / 2)
# miraudio.m:278
                    else:
                        if para.extract(4) == 2:
                            shift=size(tk,1)
# miraudio.m:280
                    if para.extract(3):
                        shift=tk(shift,1,1)
# miraudio.m:283
                    t1=t1 + shift
# miraudio.m:285
                    t2=t2 + shift
# miraudio.m:286
                if para.extract(3):
                    ft=find(tk >= logical_and(t1,tk) <= t2)
# miraudio.m:289
                else:
                    if not_(t1):
                        warning('WARNING IN MIRAUDIO: Extract sample positions should be real positive integers.')
                        display('Positions incremented by one.')
                        t1=t1 + 1
# miraudio.m:294
                        t2=t2 + 1
# miraudio.m:295
                    ft=arange(t1,t2)
# miraudio.m:297
                tk=tk(ft,arange(),arange())
# miraudio.m:299
                dk=dk(ft,arange(),arange())
# miraudio.m:300
            if isfield(para,'Ch') and not_(isempty(para.Ch)):
                dk=dk(arange(),arange(),para.Ch)
# miraudio.m:303
            if isfield(para,'center') and para.center:
                dk=center(dk)
# miraudio.m:306
                a=set(a,'Centered',1)
# miraudio.m:307
            if isfield(para,'normal') and not_(isequal(para.normal,0)):
                nl=size(dk,1)
# miraudio.m:310
                nf=size(dk,2)
# miraudio.m:311
                nc=size(dk,3)
# miraudio.m:312
                if isempty(ac):
                    if strcmpi(para.normal,'RMS'):
                        ee=0
# miraudio.m:315
                        for j in arange(1,nc).reshape(-1):
                            for i in arange(1,nf).reshape(-1):
                                ee=ee + sum(dk(arange(),i,j) ** 2)
# miraudio.m:318
                        ee=sqrt(ee / nl / nc / nf)
# miraudio.m:321
                    else:
                        if strcmpi(para.normal,'Max'):
                            ee=max(max(max(abs(dk),[],1),[],2),[],3)
# miraudio.m:323
                        else:
                            mirerror('MIRAUDIO','Incorrect parameter for 'Normal' option')
                else:
                    if strcmpi(para.normal,'RMS'):
                        ee=sqrt(sum(ac.sqrsum) / ac.samples)
# miraudio.m:328
                    else:
                        if strcmpi(para.normal,'Max'):
                            ee=ac.max
# miraudio.m:330
                if ee:
                    dk=dk / repmat(ee,concat([nl,nf,nc]))
# miraudio.m:333
            if isfield(para,'trim') and not_(isequal(para.trim,0)) and not_(strcmpi(para.trim,'NoTrim')):
                if not_(para.trimthreshold):
                    para.trimthreshold = copy(0.06)
# miraudio.m:339
                trimframe=100
# miraudio.m:341
                trimhop=10
# miraudio.m:342
                nframes=floor((length(tk) - trimframe) / trimhop) + 1
# miraudio.m:343
                rms=zeros(1,nframes)
# miraudio.m:344
                ss=sum(dk,3)
# miraudio.m:345
                for j in arange(1,nframes).reshape(-1):
                    st=floor(dot((j - 1),trimhop)) + 1
# miraudio.m:347
                    rms[j]=norm(ss(arange(st,st + trimframe - 1))) / sqrt(trimframe)
# miraudio.m:348
                rms=(rms - min(rms)) / (max(rms) - min(rms))
# miraudio.m:350
                nosil=find(rms > para.trimthreshold)
# miraudio.m:351
                if strcmpi(para.trim,'Trim') or strcmpi(para.trim,'TrimStart') or strcmpi(para.trim,'TrimBegin'):
                    nosil1=min(nosil)
# miraudio.m:354
                    if nosil1 > 1:
                        nosil1=nosil1 - 1
# miraudio.m:356
                    n1=floor(dot((nosil1 - 1),trimhop)) + 1
# miraudio.m:358
                else:
                    n1=1
# miraudio.m:360
                if strcmpi(para.trim,'Trim') or strcmpi(para.trim,'TrimEnd'):
                    nosil2=max(nosil)
# miraudio.m:363
                    if nosil2 < length(rms):
                        nosil2=nosil2 + 1
# miraudio.m:365
                    n2=floor(dot((nosil2 - 1),trimhop)) + 1
# miraudio.m:367
                else:
                    n2=length(tk)
# miraudio.m:369
                tk=tk(arange(n1,n2))
# miraudio.m:371
                dk=dk(arange(n1,n2),1,arange())
# miraudio.m:372
            if isfield(para,'smoothborder') and para.smoothborder:
                Lx,Ly,Lz=size(dk,nargout=3)
# miraudio.m:375
                Lw=dot(para.smoothborder / 1000,f[k])
# miraudio.m:376
                w=ones(size(dk))
# miraudio.m:377
                l=min(floor(Lx / 2),Lw)
# miraudio.m:378
                hw=hann(dot(l,2))
# miraudio.m:379
                w[arange(1,l),arange(),arange()]=repmat(hw(arange(1,l)),concat([1,Ly,Lz]))
# miraudio.m:380
                w[arange(Lx - l + 1,Lx),arange(),arange()]=repmat(flipud(hw(arange(1,l))),concat([1,Ly,Lz]))
# miraudio.m:381
                dk=multiply(dk,w)
# miraudio.m:382
            if isfield(para,'sampling') and para.sampling:
                if and_(f[k],not_(f[k] == para.sampling)):
                    for j in arange(1,size(dk,3)).reshape(-1):
                        rk[arange(),arange(),j]=resample(dk(arange(),arange(),j),para.sampling,f[k])
# miraudio.m:387
                    dk=copy(rk)
# miraudio.m:389
                    tk=repmat((arange(0,size(dk,1) - 1)).T,concat([1,1,size(tk,3)])) / para.sampling + tk(1,arange(),arange())
# miraudio.m:390
                f[k]=para.sampling
# miraudio.m:393
            if isfield(para,'fwr') and para.fwr:
                dk=abs(dk)
# miraudio.m:396
            d[h][k]=dk
# miraudio.m:398
            t[h][k]=tk
# miraudio.m:399
            #    d{h}{k} = flipdim(d{h}{k},1);
        #end
    
    a=set(a,'Data',d,'Time',t,'Sampling',f,'Clusters',cl)
# miraudio.m:405
    a=set(a,'Extracted',0)
# miraudio.m:406
    if isfield(para,'label'):
        if isnumeric(para.label):
            n=get(a,'Name')
# miraudio.m:409
            l=cell(1,length(d))
# miraudio.m:410
            for k in arange(1,length(d)).reshape(-1):
                if para.label:
                    l[k]=n[k](para.label)
# miraudio.m:413
                else:
                    l[k]=n[k]
# miraudio.m:415
            a=set(a,'Label',l)
# miraudio.m:418
        else:
            if iscell(para.label):
                idx=mod(get(a,'Index'),length(para.label))
# miraudio.m:420
                if not_(idx):
                    idx=length(para.label)
# miraudio.m:422
                a=set(a,'Label',para.label[idx])
# miraudio.m:424
            else:
                if ischar(para.label) and logical_not(isempty(para.label)):
                    l=cell(1,length(d))
# miraudio.m:426
                    for k in arange(1,length(d)).reshape(-1):
                        l[k]=para.label
# miraudio.m:428
                    a=set(a,'Label',l)
# miraudio.m:430
    
    
@function
def beforechunk(orig=None,option=None,postoption=None,*args,**kwargs):
    varargin = beforechunk.varargin
    nargin = beforechunk.nargin

    option.normal = copy(0)
# miraudio.m:436
    a=miraudio(orig,option)
# miraudio.m:437
    d=get(a,'Data')
# miraudio.m:438
    old=get(orig,'AcrossChunks')
# miraudio.m:439
    if isempty(old):
        old.sqrsum = copy(0)
# miraudio.m:441
        old.samples = copy(0)
# miraudio.m:442
        old.max = copy(0)
# miraudio.m:443
    
    new=mircompute(crossum,d,postoption.mono)
# miraudio.m:445
    new=new[1][1]
# miraudio.m:446
    new.sqrsum = copy(old.sqrsum + new.sqrsum)
# miraudio.m:447
    new.samples = copy(old.samples + new.samples)
# miraudio.m:448
    new.max = copy(max(old.max,new.max))
# miraudio.m:449
    
@function
def crossum(d=None,mono=None,*args,**kwargs):
    varargin = crossum.varargin
    nargin = crossum.nargin

    if isnan(mono) or mono:
        d=mean(d,3)
# miraudio.m:454
    
    s.sqrsum = copy(sum(sum(sum(d ** 2))))
# miraudio.m:456
    s.samples = copy(numel(d))
# miraudio.m:457
    s.max = copy(max(max(max(abs(d)))))
# miraudio.m:458
    
@function
def eachchunk(orig=None,option=None,missing=None,*args,**kwargs):
    varargin = eachchunk.varargin
    nargin = eachchunk.nargin

    y=miraudio(orig,option)
# miraudio.m:462
    
@function
def combinechunk(old=None,new=None,*args,**kwargs):
    varargin = combinechunk.varargin
    nargin = combinechunk.nargin

    do=get(old,'Data')
# miraudio.m:466
    to=get(old,'Time')
# miraudio.m:467
    dn=get(new,'Data')
# miraudio.m:468
    tn=get(new,'Time')
# miraudio.m:469
    y=set(old,'Data',cellarray([cellarray([concat([[do[1][1]],[dn[1][1]]])])]),'Time',cellarray([cellarray([concat([[to[1][1]],[tn[1][1]]])])]))
# miraudio.m:470