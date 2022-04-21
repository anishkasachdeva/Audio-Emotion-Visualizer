# Generated with SMOP  0.41-beta
from libsmop import *
# mirdesign.m

    
@function
def mirdesign(orig=None,argin=None,option=None,postoption=None,specif=None,type_=None,*args,**kwargs):
    varargin = mirdesign.varargin
    nargin = mirdesign.nargin

    if nargin == 0:
        d.method = copy(cellarray([]))
# mirdesign.m:4
        d.argin = copy('')
# mirdesign.m:5
        d.option = copy(cellarray([]))
# mirdesign.m:6
        d.postoption = copy(cellarray([]))
# mirdesign.m:7
        d.specif = copy(struct)
# mirdesign.m:8
        d.type = copy('')
# mirdesign.m:9
        d.frame = copy(cellarray([]))
# mirdesign.m:10
        d.segment = copy(cellarray([]))
# mirdesign.m:11
        d.chunkdecomposed = copy(0)
# mirdesign.m:12
        d.size = copy(cellarray([]))
# mirdesign.m:13
        d.file = copy('')
# mirdesign.m:14
        d.channel = copy([])
# mirdesign.m:15
        d.scale = copy([])
# mirdesign.m:16
        d.sampling = copy(0)
# mirdesign.m:17
        d.length = copy(0)
# mirdesign.m:18
        d.resampling = copy(0)
# mirdesign.m:19
        d.chunksizefactor = copy(0)
# mirdesign.m:20
        d.nochunk = copy(0)
# mirdesign.m:21
        d.overlap = copy(0)
# mirdesign.m:22
        d.separate = copy(0)
# mirdesign.m:23
        d.presilence = copy(0)
# mirdesign.m:24
        d.postsilence = copy(0)
# mirdesign.m:25
        d.chunk = copy([])
# mirdesign.m:26
        d.eval = copy(0)
# mirdesign.m:27
        d.interchunk = copy([])
# mirdesign.m:28
        d.acrosschunks = copy([])
# mirdesign.m:29
        d.ready = copy(0)
# mirdesign.m:30
        d.struct = copy([])
# mirdesign.m:31
        d.stored = copy([])
# mirdesign.m:32
        d.index = copy(NaN)
# mirdesign.m:33
        d.tmpof = copy([])
# mirdesign.m:34
    else:
        if isa(orig,'mirdesign'):
            d.method = copy(orig.method)
# mirdesign.m:36
            d.argin = copy(orig.argin)
# mirdesign.m:37
            d.option = copy(orig.option)
# mirdesign.m:38
            d.postoption = copy(orig.postoption)
# mirdesign.m:39
            d.specif = copy(orig.specif)
# mirdesign.m:40
            d.type = copy(orig.type)
# mirdesign.m:41
            d.frame = copy(orig.frame)
# mirdesign.m:42
            d.segment = copy(orig.segment)
# mirdesign.m:43
            d.chunkdecomposed = copy(orig.chunkdecomposed)
# mirdesign.m:44
            d.size = copy(orig.size)
# mirdesign.m:45
            d.file = copy(orig.file)
# mirdesign.m:46
            d.channel = copy(orig.channel)
# mirdesign.m:47
            d.scale = copy(orig.scale)
# mirdesign.m:48
            d.sampling = copy(orig.sampling)
# mirdesign.m:49
            d.length = copy(orig.length)
# mirdesign.m:50
            d.resampling = copy(orig.resampling)
# mirdesign.m:51
            d.chunksizefactor = copy(orig.chunksizefactor)
# mirdesign.m:52
            d.nochunk = copy(orig.nochunk)
# mirdesign.m:53
            d.overlap = copy(orig.overlap)
# mirdesign.m:54
            d.separate = copy(orig.separate)
# mirdesign.m:55
            d.presilence = copy(orig.presilence)
# mirdesign.m:56
            d.postsilence = copy(orig.postsilence)
# mirdesign.m:57
            d.chunk = copy(orig.chunk)
# mirdesign.m:58
            d.eval = copy(orig.eval)
# mirdesign.m:59
            d.interchunk = copy(orig.interchunk)
# mirdesign.m:60
            d.acrosschunks = copy(orig.acrosschunks)
# mirdesign.m:61
            d.ready = copy(orig.ready)
# mirdesign.m:62
            d.struct = copy(orig.struct)
# mirdesign.m:63
            d.stored = copy(orig.stored)
# mirdesign.m:64
            d.index = copy(orig.index)
# mirdesign.m:65
            d.tmpof = copy(orig.tmpof)
# mirdesign.m:66
        else:
            d.method = copy(orig)
# mirdesign.m:68
            d.argin = copy(argin)
# mirdesign.m:69
            d.option = copy(option)
# mirdesign.m:70
            d.postoption = copy(postoption)
# mirdesign.m:71
            d.specif = copy(specif)
# mirdesign.m:72
            d.type = copy(type_)
# mirdesign.m:73
            if ischar(argin):
                d.frame = copy(cellarray([]))
# mirdesign.m:75
                d.segment = copy(cellarray([]))
# mirdesign.m:76
                d.chunkdecomposed = copy(0)
# mirdesign.m:77
                d.size = copy(cellarray([]))
# mirdesign.m:78
                d.file = copy('')
# mirdesign.m:79
                d.channel = copy([])
# mirdesign.m:80
                d.scale = copy([])
# mirdesign.m:81
                d.sampling = copy(0)
# mirdesign.m:82
                d.length = copy(0)
# mirdesign.m:83
                d.resampling = copy(0)
# mirdesign.m:84
                d.chunksizefactor = copy(1)
# mirdesign.m:85
                d.nochunk = copy(0)
# mirdesign.m:86
                d.overlap = copy(0)
# mirdesign.m:87
                d.separate = copy(0)
# mirdesign.m:88
                d.presilence = copy(0)
# mirdesign.m:89
                d.postsilence = copy(0)
# mirdesign.m:90
            else:
                if iscell(argin):
                    argin=argin[1]
# mirdesign.m:93
                if (strcmp(func2str(orig),'mirspectrum') and d.option.alongbands) or (isfield(specif,'nochunk') and specif.nochunk):
                    d.frame = copy([])
# mirdesign.m:97
                    if isfield(d.specif,'eachchunk'):
                        d.specif = copy(rmfield(d.specif,'eachchunk'))
# mirdesign.m:99
                        d.specif = copy(rmfield(d.specif,'combinechunk'))
# mirdesign.m:100
                else:
                    d.frame = copy(argin.frame)
# mirdesign.m:103
                    if not_(isempty(d.frame)):
                        if isfield(d.specif,'extensive'):
                            d.frame.dontchunk = copy(1)
# mirdesign.m:106
                            # chunk after chunk because the whole result is needed for
                    # subsequent computations.
                        else:
                            if isfield(d.specif,'chunkframebefore'):
                                d.frame.chunkbefore = copy(1)
# mirdesign.m:111
                d.segment = copy(argin.segment)
# mirdesign.m:115
                d.chunkdecomposed = copy(argin.chunkdecomposed)
# mirdesign.m:116
                d.size = copy(argin.size)
# mirdesign.m:117
                d.file = copy(argin.file)
# mirdesign.m:118
                d.channel = copy(argin.channel)
# mirdesign.m:119
                d.scale = copy(argin.scale)
# mirdesign.m:120
                d.sampling = copy(argin.sampling)
# mirdesign.m:121
                d.length = copy(argin.length)
# mirdesign.m:122
                d.resampling = copy(argin.resampling)
# mirdesign.m:123
                d.chunksizefactor = copy(argin.chunksizefactor)
# mirdesign.m:124
                if (isfield(specif,'nochunk') and specif.nochunk):
                    d.nochunk = copy(1)
# mirdesign.m:126
                else:
                    if not_(isempty(argin.stored)):
                        # a temporary variable will be already computed.
                        d.nochunk = copy(2)
# mirdesign.m:129
                        # performed. Temporary variables cannot for the 
                           # moment be dispatched to dependent variables 
                           # chunk by chunk, but only once the whole 
                           # variable has been computed.
                    else:
                        d.nochunk = copy(argin.nochunk)
# mirdesign.m:135
                d.chunksizefactor = copy(argin.chunksizefactor)
# mirdesign.m:137
                d.overlap = copy(argin.overlap)
# mirdesign.m:138
                d.separate = copy(argin.separate)
# mirdesign.m:139
                d.presilence = copy(argin.presilence)
# mirdesign.m:140
                d.postsilence = copy(argin.postsilence)
# mirdesign.m:141
            d.chunk = copy([])
# mirdesign.m:143
            d.eval = copy(0)
# mirdesign.m:144
            d.interchunk = copy([])
# mirdesign.m:145
            d.acrosschunks = copy([])
# mirdesign.m:146
            d.ready = copy(0)
# mirdesign.m:147
            d.struct = copy([])
# mirdesign.m:148
            d.stored = copy([])
# mirdesign.m:149
            d.index = copy(NaN)
# mirdesign.m:150
            d.tmpof = copy([])
# mirdesign.m:151
    
    d=class_(d,'mirdesign')
# mirdesign.m:153