# Generated with SMOP  0.41-beta
from libsmop import *
# mirfunction.m

    
@function
def mirfunction(method=None,x=None,varg=None,nout=None,specif=None,init=None,main=None,*args,**kwargs):
    varargin = mirfunction.varargin
    nargin = mirfunction.nargin

    # Meta function called by all MIRtoolbox functions.
# Integrates the function into the general flowchart
#   and eventually launches the "mireval" evaluation process.
# Here are the successive steps in the following code:
#   - If the input is an audio filename, instantiates a new design flowchart.
#   - Reads all the options specified by the user.
#   - Performs the 'init' part of the MIRtoolbox function:
#       - If the input is a design flowchart,
#           add the 'init' part in the flowchart.
#       - If the input is some MIRtoolbox data,
#           execute the 'init' part on that data.
#   - Performs the 'main' part of the MIRtoolbox function.
    
    if isempty(x):
        o=cellarray([cellarray([]),cellarray([]),cellarray([])])
# mirfunction.m:16
        return o
    
    if ischar(x) or (iscell(x) and ischar(x[1])):
        # Starting point of the design process
        design_init=1
# mirfunction.m:23
        filename=copy(x)
# mirfunction.m:24
        if strcmpi(func2str(method),'miraudio'):
            postoption=cellarray([])
# mirfunction.m:26
        else:
            postoption.mono = copy(1)
# mirfunction.m:28
        orig=mirdesign(miraudio,'Design',cellarray([varg]),postoption,struct,'miraudio')
# mirfunction.m:30
    else:
        if isnumeric(x) and logical_not(isequal(method,mirsimatrix)):
            mirerror(func2str(method),'The input should be a file name or a MIRtoolbox object.')
        else:
            design_init=0
# mirfunction.m:35
            orig=copy(x)
# mirfunction.m:36
    
    # Reads all the options specified by the user.
    orig,during,after=miroptions(method,orig,specif,varg,nargout=3)
# mirfunction.m:40
    # Performs the 'init' part of the MIRtoolbox function.
    if isa(orig,'mirdesign'):
        if not_(get(orig,'Eval')):
            # Top-down construction of the general design flowchart
            if isstruct(during) and isfield(during,'frame') and isstruct(during.frame) and during.frame.auto:
                # 'Frame' option: 
            # Automatic insertion of the mirframe step in the design
                orig=mirframe(orig,during.frame.length.val,during.frame.length.unit,during.frame.hop.val,during.frame.hop.unit,during.frame.phase.val,during.frame.phase.unit,during.frame.phase.atend)
# mirfunction.m:51
            # The 'init' part of the function can be integrated into the design
        # flowchart. This leads to a top-down construction of the
        # flowchart.
        # Automatic development of the implicit prerequisites,
        # with management of the data types throughout the design process.
            orig,type_=init(orig,during,nargout=2)
# mirfunction.m:65
            o=mirdesign(method,orig,during,after,specif,type_)
# mirfunction.m:67
            if design_init and not_(ischar(filename) and strcmpi(filename,'Design')):
                # Now the design flowchart has been completed created.
            # If the 'Design' keyword not used,
            # the function is immediately evaluated
                o=mireval(o,filename,nout)
# mirfunction.m:74
            else:
                o=returndesign(o,nout)
# mirfunction.m:76
            if not_(iscell(o)):
                o=cellarray([o])
# mirfunction.m:79
            return o
        else:
            # During the top-down traversal of the flowchart (evaleach), at the
        # beginning of the evaluation process.
            orig,x=evaleach(orig,nargout=2)
# mirfunction.m:86
            if not_(isequal(method,nthoutput)):
                if iscell(orig):
                    orig=orig[1]
# mirfunction.m:90
                if isempty(get(orig,'InterChunk')):
                    orig=set(orig,'InterChunk',get(x,'InterChunk'))
# mirfunction.m:93
    else:
        design=0
# mirfunction.m:98
        if iscell(orig):
            i=0
# mirfunction.m:100
            while i < length(orig) and not_(design):

                i=i + 1
# mirfunction.m:102
                if isa(orig[i],'mirdesign'):
                    design=copy(i)
# mirfunction.m:104

        if design:
            # For function with multiple inputs
            if design == 1 and not_(get(orig[1],'Eval')):
                # Progressive construction of the general design
                orig,type_=init(orig,during,nargout=2)
# mirfunction.m:112
                o=mirdesign(method,orig,during,after,specif,type_)
# mirfunction.m:113
                o=set(o,'Size',get(orig[1],'Size'))
# mirfunction.m:114
                o=returndesign(o,nout)
# mirfunction.m:115
                return o
            else:
                # Evaluation of the design.
            # First top-down initiation (evaleach), then bottom-up process.
                for io in arange(1,length(orig)).reshape(-1):
                    if isa(orig[io],'mirdesign'):
                        o=evaleach(orig[io])
# mirfunction.m:122
                        if iscell(o):
                            o=o[arange()]
# mirfunction.m:124
                        orig[io]=o
# mirfunction.m:126
        else:
            if not_(isempty(init)) and not_(isempty(during)):
                if isstruct(during) and isfield(during,'frame') and isstruct(during.frame) and during.frame.auto:
                    orig=mirframe(orig,during.frame.length,during.frame.hop,during.frame.phase,during.frame.presilence,during.frame.postsilence)
# mirfunction.m:133
                # The input of the function is not a design flowchart, which
        # the 'init' part of the function could be integrated into.
            # (cf. previous call of 'init' in this script). 
        # For that reason, the 'init' part of the function needs to be
        # evaluated now.
                orig=init(orig,during)
# mirfunction.m:144
    
    # Performs the 'main' part of the MIRtoolbox function.
    if not_(iscell(orig) and not_(ischar(orig[1]))) and not_(isa(orig,'mirdesign') or isa(orig,'mirdata')):
        o=cellarray([orig])
# mirfunction.m:151
        return o
    
    filenamearg=copy(orig)
# mirfunction.m:154
    if iscell(filenamearg) and not_(ischar(filenamearg[1])):
        filenamearg=filenamearg[1]
# mirfunction.m:156
    
    if iscell(filenamearg) and not_(ischar(filenamearg[1])):
        filenamearg=filenamearg[1]
# mirfunction.m:159
    
    filename=get(filenamearg,'Name')
# mirfunction.m:161
    if not_(isempty(during)) and mirverbose:
        if length(filename) == 1:
            disp(concat(['Computing ',func2str(method),' related to ',filename[1],'...']))
        else:
            disp(concat(['Computing ',func2str(method),' for all audio files ...']))
    
    if iscell(x):
        x1=x[1]
# mirfunction.m:170
    else:
        x1=copy(x)
# mirfunction.m:172
    
    if not_(iscell(orig) or isnumeric(x)):
        orig=set(orig,'Index',get(x1,'Index'))
# mirfunction.m:175
    
    if iscell(orig):
        o=main(orig,during,after)
# mirfunction.m:178
    else:
        d=get(orig,'Data')
# mirfunction.m:180
        if isamir(orig,'miraudio') and length(d) == 1 and length(d[1]) == 1 and isempty(d[1][1]):
            # To solve a problem when MP3read returns empty chunk.
        # Warning: it should not be a cell, because for instance nthoutput can have first input empty...
            o=copy(orig)
# mirfunction.m:185
        else:
            o=main(orig,during,after)
# mirfunction.m:187
    
    if not_(iscell(o) and length(o) > 1) or (isa(x,'mirdesign') and get(x,'Eval')):
        o=cellarray([o,x])
# mirfunction.m:191
    else:
        if iscell(x) and isa(x[1],'mirdesign') and get(x[1],'Eval'):
            o=cellarray([o,x])
# mirfunction.m:193
        else:
            if not_(isempty(varg)) and isstruct(varg[1]) and not_(iscell(o) and iscell(o[1])):
                # When the function was called by mireval, the output should be packed
    # into one single cell array (in order to be send back to calling
    # routines).
                o=cellarray([o])
# mirfunction.m:199
    
    
@function
def returndesign(i=None,nout=None,*args,**kwargs):
    varargin = returndesign.varargin
    nargin = returndesign.nargin

    o=cell(1,nout)
# mirfunction.m:204
    o[1]=i
# mirfunction.m:205
    for k in arange(2,nout).reshape(-1):
        o[k]=nthoutput(i,k)
# mirfunction.m:207
    