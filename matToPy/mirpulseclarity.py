# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m

    
@function
def mirpulseclarity(orig=None,varargin=None,*args,**kwargs):
    varargin = mirpulseclarity.varargin
    nargin = mirpulseclarity.nargin

    #   r = mirpulseclarity(x) estimates the rhythmic clarity, indicating the
#       strength of the beats estimated by the mirtempo function.
#   Optional arguments:
#       mirpulseclarity(...,s): specifies a strategy for pulse clarity
#           estimation.
#           Possible values: 'MaxAutocor' (default), 'MinAutocor',
#               'KurtosisAutocor', MeanPeaksAutocor', 'EntropyAutocor', 
#               'InterfAutocor', 'TempoAutocor', 'ExtremEnvelop', 
#               'Attack', 'Articulation'
#       mirpulseclarity(...,'Frame',l,h): orders a frame decomposition of
#           the audio input of window length l (in seconds) and hop factor
#           h, expressed relatively to the window length.
#           Default values: l = 5 seconds and h = .1
#       Onset detection strategies: 'Envelope' (default), 'DiffEnvelope', 
#           'SpectralFlux', 'Pitch'.
#       Options related to the autocorrelation computation can be specified
#           as well: 'Min', 'Max', 'Resonance', 'Enhanced'
#       Options related to the tempo estimation can be specified here
#           as well: 'Sum', 'Total', 'Contrast'.
#       cf. User's Manual for more details.
#   [r,a] = mirpulseclarity(x) also returns the beat autocorrelation.
    
    model.key = copy('Model')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:24
    model.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:25
    model.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:26
    option.model = copy(model)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:27
    stratg.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:29
    stratg.choice = copy(cellarray(['MaxAutocor','MinAutocor','MeanPeaksAutocor','KurtosisAutocor','EntropyAutocor','InterfAutocor','TempoAutocor','ExtremEnvelop','Attack','Articulation']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:30
    stratg.default = copy('MaxAutocor')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:34
    option.stratg = copy(stratg)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:35
    frame.key = copy('Frame')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:37
    frame.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:38
    frame.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:39
    frame.keydefault = copy(concat([5,0.1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:40
    frame.default = copy(concat([0,0]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:41
    option.frame = copy(frame)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:42
    ## options related to mironsets:
    
    fea.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:46
    fea.choice = copy(cellarray(['Envelope','DiffEnvelope','SpectralFlux','Pitch']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:47
    fea.default = copy('Envelope')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:48
    option.fea = copy(fea)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:49
    
    
    envmeth.key = copy('Method')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:54
    envmeth.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:55
    envmeth.choice = copy(cellarray(['Filter','Spectro']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:56
    envmeth.default = copy('Spectro')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:57
    option.envmeth = copy(envmeth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:58
    
    ftype.key = copy('FilterType')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:62
    ftype.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:63
    ftype.choice = copy(cellarray(['IIR','HalfHann']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:64
    ftype.default = copy('IIR')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:65
    option.ftype = copy(ftype)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:66
    fb.key = copy('Filterbank')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:68
    fb.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:69
    fb.default = copy(20)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:70
    option.fb = copy(fb)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:71
    fbtype.key = copy('FilterbankType')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:73
    fbtype.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:74
    fbtype.choice = copy(cellarray(['Gammatone','Scheirer','Klapuri']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:75
    fbtype.default = copy('Scheirer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:76
    option.fbtype = copy(fbtype)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:77
    
    band.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:81
    band.choice = copy(cellarray(['Freq','Mel','Bark','Cents']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:82
    band.default = copy('Freq')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:83
    option.band = copy(band)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:84
    diffhwr.key = copy('HalfwaveDiff')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:87
    diffhwr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:88
    diffhwr.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:89
    diffhwr.keydefault = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:90
    option.diffhwr = copy(diffhwr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:91
    lambda_.key = copy('Lambda')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:93
    lambda_.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:94
    lambda_.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:95
    option.lambda = copy(lambda_)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:96
    aver.key = copy('Smooth')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:98
    aver.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:99
    aver.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:100
    aver.keydefault = copy(30)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:101
    option.aver = copy(aver)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:102
    oplog.key = copy('Log')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:104
    oplog.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:105
    oplog.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:106
    option.log = copy(oplog)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:107
    mu.key = copy('Mu')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:109
    mu.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:110
    mu.default = copy(100)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:111
    option.mu = copy(mu)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:112
    
    
    inc.key = copy('Inc')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:116
    inc.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:117
    inc.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:118
    option.inc = copy(inc)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:119
    median.key = copy('Median')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:121
    median.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:122
    median.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:123
    median.default = copy(concat([0,0]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:124
    
    option.median = copy(median)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:125
    hw.key = copy('Halfwave')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:127
    hw.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:128
    hw.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:129
    
    option.hw = copy(hw)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:130
    ## options related to mirattackslope
    slope.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:134
    slope.choice = copy(cellarray(['Diff','Gauss']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:135
    slope.default = copy('Diff')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:136
    option.slope = copy(slope)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:137
    ## options related to mirautocor:
    
    enh.key = copy('Enhanced')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:141
    enh.type = copy('Integers')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:142
    enh.default = copy([])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:143
    enh.keydefault = copy(arange(2,10))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:144
    option.enh = copy(enh)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:145
    r.key = copy('Resonance')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:147
    r.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:148
    r.choice = copy(cellarray(['ToiviainenSnyder','vonNoorden',0,'off','no']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:149
    r.default = copy('ToiviainenSnyder')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:150
    option.r = copy(r)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:151
    mi.key = copy('Min')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:153
    mi.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:154
    mi.default = copy(40)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:155
    option.mi = copy(mi)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:156
    ma.key = copy('Max')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:158
    ma.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:159
    ma.default = copy(200)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:160
    option.ma = copy(ma)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:161
    ## options related to mirtempo:
    
    sum.key = copy('Sum')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:165
    sum.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:166
    sum.choice = copy(cellarray(['Before','After','Adjacent']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:167
    sum.default = copy('Before')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:168
    option.sum = copy(sum)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:169
    m.key = copy('Total')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:171
    m.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:172
    m.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:173
    option.m = copy(m)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:174
    thr.key = copy('Contrast')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:176
    thr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:177
    thr.default = copy(0.01)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:178
    
    option.thr = copy(thr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:179
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:181
    varargout=mirfunction(mirpulseclarity,orig,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:183
    ## Initialisation
    
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    #if isframed(x)
#    warning('WARNING IN MIRPULSECLARITY: The input should not be already decomposed into frames.');
#    disp(['Suggestion: Use the ''Frame'' option instead.'])
#end
    if iscell(x):
        x=x[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:195
    
    if isamir(x,'mirautocor'):
        type_=cellarray(['mirscalar','mirautocor'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:198
    else:
        if length(option.model) > 1:
            a=copy(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:200
            type_=cellarray(['mirscalar'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:201
            for m in arange(1,length(option.model)).reshape(-1):
                if option.frame.length.val:
                    y=mirpulseclarity(a,'Model',option.model(m),'Frame',option.frame.length.val,option.frame.length.unit,option.frame.hop.val,option.frame.hop.unit)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:204
                else:
                    y=mirpulseclarity(a,'Model',option.model(m))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:210
                if m == 1:
                    x=copy(y)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:213
                else:
                    x=x + y
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:215
        else:
            if option.model:
                if 1 == option.model:
                    pass
                else:
                    if 2 == option.model:
                        option.envmeth = copy('Filter')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:223
                        option.fbtype = copy('Gammatone')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:224
                        option.mu = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:225
                        option.r = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:226
                        option.lambda = copy(0.8)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:227
                        option.sum = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:228
            if length(option.stratg) > 7 and strcmpi(option.stratg(arange(end() - 6,end())),'Autocor'):
                if (strcmpi(option.stratg,'MaxAutocor') or strcmpi(option.stratg,'MinAutocor') or strcmpi(option.stratg,'EntropyAutocor')):
                    option.m = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:235
                if strcmpi(option.stratg,'MinAutocor'):
                    option.enh = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:238
                if option.frame.length.val:
                    t,x=mirtempo(x,option.fea,'Method',option.envmeth,option.band,'Sum',option.sum,'Enhanced',option.enh,'Resonance',option.r,'Smooth',option.aver,'HalfwaveDiff',option.diffhwr,'Lambda',option.lambda,'Frame',option.frame.length.val,option.frame.length.unit,option.frame.hop.val,option.frame.hop.unit,'FilterbankType',option.fbtype,'FilterType',option.ftype,'Filterbank',option.fb,'Mu',option.mu,'Log',option.log,'Inc',option.inc,'Halfwave',option.hw,'Median',option.median(1),option.median(2),'Min',option.mi,'Max',option.ma,'Total',option.m,'Contrast',option.thr,nargout=2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:241
                else:
                    t,x=mirtempo(x,option.fea,'Method',option.envmeth,option.band,'Sum',option.sum,'Enhanced',option.enh,'Resonance',option.r,'Smooth',option.aver,'HalfwaveDiff',option.diffhwr,'Lambda',option.lambda,'FilterbankType',option.fbtype,'FilterType',option.ftype,'Filterbank',option.fb,'Mu',option.mu,'Log',option.log,'Inc',option.inc,'Halfwave',option.hw,'Median',option.median(1),option.median(2),'Min',option.mi,'Max',option.ma,'Total',option.m,'Contrast',option.thr,nargout=2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:260
                type_=cellarray(['mirscalar','mirautocor'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:275
            else:
                if strcmpi(option.stratg,'ExtremEnvelop'):
                    x=mironsets(x,'Filterbank',option.fb)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:277
                    type_=cellarray(['mirscalar','mirenvelope'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:278
                else:
                    if strcmpi(option.stratg,'Attack'):
                        x=mirattackslope(x,option.slope)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:280
                        type_=cellarray(['mirscalar','mirenvelope'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:281
                        #    elseif strcmpi(option.stratg,'AttackDiff')
#        type = {'mirscalar','mirenvelope'};
                    else:
                        if strcmpi(option.stratg,'Articulation'):
                            x=mirlowenergy(x,'ASR')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:285
                            type_=cellarray(['mirscalar','mirscalar'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:286
                        else:
                            type_=cellarray(['mirscalar','miraudio'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:288
    
    ## Main function
    
    
@function
def main(a=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if option.model == 2:
        option.stratg = copy('InterfAutocor')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:298
    
    if isa(a,'mirscalar') and not_(strcmpi(option.stratg,'Attack')):
        o=cellarray([a])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:301
        return o
    
    if option.m == 1 and (strcmpi(option.stratg,'InterfAutocor') or strcmpi(option.stratg,'MeanPeaksAutocor')):
        option.m = copy(Inf)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:307
    
    if iscell(a):
        a=a[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:310
    
    if strcmpi(option.stratg,'MaxAutocor'):
        d=get(a,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:313
        rc=mircompute(max,d)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:314
    else:
        if strcmpi(option.stratg,'MinAutocor'):
            d=get(a,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:316
            rc=mircompute(minusmin,d)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:317
        else:
            if strcmpi(option.stratg,'MeanPeaksAutocor'):
                m=get(a,'PeakVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:319
                rc=mircompute(meanpeaks,m)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:320
            else:
                if strcmpi(option.stratg,'KurtosisAutocor'):
                    a=mirpeaks(a,'Extract','Total',option.m,'NoBegin','NoEnd')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:322
                    k=mirkurtosis(a)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:323
                    #rc = mircompute(@meanpeaks,d);
                    rc=mirmean(k)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:326
                else:
                    if strcmpi(option.stratg,'EntropyAutocor'):
                        rc=mirentropy(a)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:328
                    else:
                        if strcmpi(option.stratg,'InterfAutocor'):
                            a=mirpeaks(a,'Total',option.m,'NoBegin','NoEnd')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:330
                            m=get(a,'PeakVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:331
                            p=get(a,'PeakPosUnit')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:332
                            rc=mircompute(interf,m,p)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:333
                        else:
                            if strcmpi(option.stratg,'TempoAutocor'):
                                a=mirpeaks(a,'Total',1,'NoBegin','NoEnd')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:335
                                p=get(a,'PeakPosUnit')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:336
                                rc=mircompute(tempo,p)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:337
                            else:
                                if strcmpi(option.stratg,'ExtremEnvelop'):
                                    a=mirenvelope(a,'Normal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:339
                                    p=mirpeaks(a,'Order','Abscissa')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:340
                                    p=get(p,'PeakPreciseVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:341
                                    n=mirpeaks(a,'Valleys','Order','Abscissa')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:342
                                    n=get(n,'PeakPreciseVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:343
                                    rc=mircompute(shape,p,n)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:344
                                else:
                                    if strcmpi(option.stratg,'Attack'):
                                        rc=mirmean(a)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:346
                                        #elseif strcmpi(option.stratg,'AttackDiff')
#    a = mirpeaks(a);
#    m = get(a,'PeakVal');
#    rc = mircompute(@meanpeaks,m);
                                    else:
                                        if strcmpi(option.stratg,'Articulation'):
                                            rc=copy(a)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:352
    
    if iscell(rc):
        pc=mirscalar(a,'Data',rc,'Title','Pulse clarity')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:356
    else:
        pc=set(rc,'Title',concat(['Pulse clarity (',get(rc,'Title'),')']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:358
    
    if option.model:
        if 1 == option.model:
            alpha=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:364
            beta=2.2015
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:365
            lambda_=0.1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:366
        else:
            if 2 == option.model:
                alpha=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:368
                beta=3.5982
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:369
                lambda_=1.87
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:370
        if not_(lambda_ == 0):
            pc=dot((pc + alpha) ** lambda_,beta)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:373
        else:
            pc=dot(log(pc + alpha),beta)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:375
        title=concat(['Pulse clarity (Model ',num2str(option.model),')'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:377
        pc=set(pc,'Title',title)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:378
    
    o=cellarray([pc,a])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:381
    ## Routines
    
    
@function
def shape(p=None,n=None,*args,**kwargs):
    varargin = shape.varargin
    nargin = shape.nargin

    p=p[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:387
    n=n[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:388
    if length(p) > length(n):
        d=sum(p(arange(1,end() - 1)) - n) + sum(p(arange(2,end())) - n)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:390
        r=d / (dot(2,length(n)))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:391
    else:
        if length(p) < length(n):
            d=sum(p - n(arange(1,end() - 1))) + sum(p - n(arange(2,end())))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:393
            r=d / (dot(2,length(p)))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:394
        else:
            d=sum(p(arange(2,end())) - n(arange(1,end() - 1))) + sum(p(arange(1,end() - 1)) - n(arange(2,end())))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:396
            r=d / (dot(2,(length(p) - 1)))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:397
    
    
@function
def minusmin(ac=None,*args,**kwargs):
    varargin = minusmin.varargin
    nargin = minusmin.nargin

    rc=- min(ac)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:402
    
@function
def meanpeaks(ac=None,*args,**kwargs):
    varargin = meanpeaks.varargin
    nargin = meanpeaks.nargin

    rc=zeros(1,length(ac))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:406
    for j in arange(1,length(ac)).reshape(-1):
        if isempty(ac[j]):
            rc[j]=NaN
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:409
        else:
            rc[j]=mean(ac[j])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:411
    
    
@function
def interf(mk=None,pk=None,*args,**kwargs):
    varargin = interf.varargin
    nargin = interf.nargin

    rc=zeros(size(mk))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:417
    for j in arange(1,size(mk,3)).reshape(-1):
        for i in arange(1,size(mk,2)).reshape(-1):
            pij=pk[1,i,j]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:420
            mij=mk[1,i,j]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:421
            if isempty(pij):
                rc[1,i,j]=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:423
            else:
                high=max(pij(arange(2,end())),pij(1))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:425
                low=min(pij(arange(2,end())),pij(1))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:426
                quo=rem(high,low) / low
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:427
                nomult=quo > logical_and(0.15,quo) < 0.85
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:428
                fij=multiply(mij(arange(2,end())) / mij(1),nomult)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:429
                fij[fij < 0]=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:430
                rc[1,i,j]=exp(- sum(fij) / 4)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:431
                # with dominant pulse decrease clarity
    
    
@function
def tempo(pk=None,*args,**kwargs):
    varargin = tempo.varargin
    nargin = tempo.nargin

    rc=zeros(size(pk))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:439
    for j in arange(1,size(pk,3)).reshape(-1):
        for i in arange(1,size(pk,2)).reshape(-1):
            pij=pk[1,i,j]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:442
            if isempty(pij):
                rc[1,i,j]=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:444
            else:
                rc[1,i,j]=exp(- pij(1) / 4) / exp(- 0.33 / 4)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirpulseclarity.m:446
                # increases clarity
    