# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m

    
@function
def mirnovelty(orig=None,varargin=None,*args,**kwargs):
    varargin = mirnovelty.varargin
    nargin = mirnovelty.nargin

    # n = mirnovelty(m) evaluates the novelty score from a similarity matrix.
# By default, if the 'Kernel' (or 'KernelSize') option is not specified, 
#   our new multi-granular strategy for novelty computation is used. It is 
#   a simpler but more powerful and general method that automatically 
#   detects homogeneous segments of any size.
    
    # When this default multi-granular approach is used for academic research, 
#   please cite the following publication:
# Lartillot, O., Cereghetti, D., Eliard, K., Grandjean, D., ?A simple, 
#   high-yield method for assessing structural novelty?, International 
#   Conference on Music and Emotion, Jyv�skyl�, 2013.
    
    #   Optional argument: 
#       mirnovelty(...,'Distance',f) specifies the name of a dissimilarity
#           distance function, from those proposed in the Statistics Toolbox
#               (help pdist).
#           default value: f = 'cosine'
#       mirnovelty(...,'Similarity',f) specifies the name of a similarity
#           measure function. This function is applied to the result of the
#           distance function. cf. mirsimatrix 
#           default value: f = 'exponential'
#               corresponding to f(x) = exp(-x)
#       mirnovelty(...,'KernelSize',s) selects the kernel-based method and
#           specifies the length of the gaussian kernel, in samples.
#       mirnovelty(...,'Normal',0) does not normalize the novelty curve
#           between the values 0 and 1.
#       mirnovelty(...,'Horizontal') uses the 'Horizontal' option in
#           mirsimatrix instead of 'TimeLag' used here by default.
    
    #   [n,m] = mirnovelty(m) also return the similarity matrix.
    
    #   Foote, J. & Cooper, M. (2003). Media Segmentation using Self-Similarity
# Decomposition,. In Proc. SPIE Storage and Retrieval for Multimedia
# Databases, Vol. 5021, pp. 167-75.
    
    dist.key = copy('Distance')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:37
    dist.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:38
    dist.default = copy('cosine')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:39
    option.dist = copy(dist)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:40
    sm.key = copy(cellarray(['Measure','Similarity']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:42
    sm.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:43
    sm.default = copy('exponential')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:44
    option.sm = copy(sm)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:45
    K.key = copy(cellarray(['KernelSize','Width','Kernel']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:47
    K.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:48
    K.default = copy(Inf)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:49
    option.K = copy(K)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:50
    #        gran.key = 'Granul';
#        gran.type = 'Integer';
#        gran.default = 1;
#    option.gran = gran;
    
    transf.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:57
    transf.default = copy('Standard')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:58
    transf.choice = copy(cellarray(['Horizontal','TimeLag','Standard']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:59
    option.transf = copy(transf)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:60
    flux.key = copy('Flux')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:62
    flux.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:63
    flux.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:64
    option.flux = copy(flux)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:65
    simple.key = copy('Simple')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:67
    simple.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:68
    simple.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:69
    option.simple = copy(simple)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:70
    half.key = copy('Half')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:72
    half.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:73
    half.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:74
    option.half = copy(half)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:75
    cluster.key = copy('Cluster')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:77
    cluster.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:78
    cluster.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:79
    option.cluster = copy(cluster)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:80
    normal.key = copy('Normal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:82
    normal.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:83
    normal.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:84
    normal.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:85
    option.normal = copy(normal)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:86
    filterborder.key = copy('FilterBorder')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:88
    filterborder.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:89
    filterborder.default = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:90
    filterborder.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:91
    option.filterborder = copy(filterborder)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:92
    direct.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:94
    direct.default = copy('Both')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:95
    direct.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:96
    direct.choice = copy(cellarray(['Both','Forth','Back']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:97
    option.direct = copy(direct)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:98
    integr.key = copy('Integrate')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:100
    integr.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:101
    integr.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:102
    integr.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:103
    option.integr = copy(integr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:104
    filter.key = copy('Filter')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:106
    filter.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:107
    filter.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:108
    filter.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:109
    option.filter = copy(filter)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:110
    frame.key = copy('Frame')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:112
    frame.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:113
    frame.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:114
    frame.default = copy(concat([0.05,1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:115
    option.frame = copy(frame)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:116
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:118
    specif.nochunk = copy(1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:119
    varargout=mirfunction(mirnovelty,orig,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:120
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    type_='mirscalar'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:124
    if logical_not(option.simple) and not_(isamir(x,'mirscalar') and strcmp(get(x,'Title'),'Novelty')):
        if logical_not(isinf(option.K)):
            option.half = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:129
            if strcmpi(option.transf,'Standard'):
                option.transf = copy('TimeLag')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:131
            #elseif isinf(option.K)
    #    option.transf = 'TimeLag';
        x=mirsimatrix(x,'Distance',option.dist,'Similarity',option.sm,'Width',max(option.K),option.transf,'Half',option.half,'Cluster',option.cluster,'Frame',option.frame.length.val,option.frame.length.unit,option.frame.hop.val,option.frame.hop.unit,option.frame.phase.val,option.frame.phase.unit)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:137
    
    
@function
def main(orig=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(orig):
        orig=orig[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:148
    
    if isa(orig,'mirscalar'):
        score=get(orig,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:152
    else:
        if option.simple:
            d=get(orig,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:155
            for i in arange(1,length(d)).reshape(-1):
                for j in arange(1,length(d[i])).reshape(-1):
                    buf=zeros(size(d[i][j],1),1,size(d[i][j],3),size(d[i][j],4))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:158
                    for k in arange(1,size(d[i][j],2)).reshape(-1):
                        score[i][j][k]=sum(max(d[i][j](arange(),k,arange(),arange()) - buf,0) ** 3)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:160
                        buf=max(d[i][j](arange(),k,arange(),arange()),buf)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:161
                        low=find(d[i][j](arange(),k) < 0.001)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:162
                        buf[low]=d[i][j](low,k)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:163
                    score[i][j]=atan(dot((score[i][j] / max(score[i][j])),20))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:165
            n=mirscalar(orig,'Data',score,'Title','Novelty')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:168
        else:
            if isinf(option.K):
                s=get(orig,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:171
                for i in arange(1,length(s)).reshape(-1):
                    for j in arange(1,length(s[i])).reshape(-1):
                        #sij0 = s{i}{j}(:);
            #sij0(sij0 == 1) = [];
            #Msij = max(sij0);
            #msij = min(sij0);
            #k0 = 1;
                        score[i][j]=zeros(1,size(s[i][j],2))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:180
                        for k in arange(3,size(s[i][j],2)).reshape(-1):
                            #delt = min(k-2,dw+1);
                #dist = NaN(1,delt);
                #for l = 1:delt
                            l=1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:185
                            bloc=s[i][j](arange(k - l - 1,1,- 1),arange(1,k - l))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:186
                            stop=find(s[i][j](arange(k - l - 1,1,- 1),k) > min(s[i][j](arange(k - l - 1,1,- 1),k - l),max(mean(bloc,2) - dot(2,std(bloc,0,2)),min(bloc,[],2))))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:187
                            if length(stop) < 2:
                                stop=k - l
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:192
                            else:
                                stop[end() + 1]=stop(end()) + 1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:194
                                stopp=find(diff(stop(arange(1,end() - 1))) == logical_and(1,diff(stop,2)) == 0,1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:195
                                if isempty(stopp):
                                    stop=k - l
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:197
                                else:
                                    stop=stop(stopp)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:199
                            if logical_not(isempty(stop)):
                                #dist(l) = ... stop * ...
                                dist=sum(diff(concat([s[i][j](arange(k - l - stop + 1,k - l - 1),k),s[i][j](arange(k - l - stop + 1,k - l - 1),k - l)]),1,2))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:204
                                #.*((s{i}{j}(k-l-stop:k-l-1,k-1) - msij)...
                                      #   /(Msij-msij)).^1); ...
                                  #/ max(k-1, 100);
                            #if l == 1
                    #    dist0 = dist(l);
                    #end
                    #if l > 1 && dist(l) > dist(l0) && k-l >= k0
                    #    dist(l0) = dist(l);
                    #    dist(l) = 0;
                    #else
                    #    l0 = l;
                    #    if l > 1 && k-l >= k0
                    #        dist(l0) = dist0;
                    #        k0 = k-1;
                    #    end
                    #end
                #end
                #best = 0;
                #for l = 1:delt
                    #dist(l) = dist(l) + (l-1)/(dw+1);
                #    if dist(l) > best
                #        best = dist(l);
                #        bestl = l;
                #    end
                #end
                            score[i][j][k]=max(dist,0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:233
                            #if bestl > 1
                #    score{i}{j}(k-1:k-bestl+1) = ...
                #        min(score{i}{j}(k-1:k-bestl+1),best);
                #end
                n=mirscalar(orig,'Data',score,'Title','Novelty')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:241
            else:
                if option.flux:
                    fl=mirflux(orig)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:244
                    if 1:
                        n=mirscalar(fl,'Title','Novelty')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:246
                    else:
                        score=get(fl,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:248
                        dw=get(orig,'DiagWidth')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:249
                        if dw < Inf and not_(isempty(postoption)) and postoption.normal:
                            for k in arange(1,length(score)).reshape(-1):
                                for l in arange(1,length(score[k])).reshape(-1):
                                    lg=length(score[k][l])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:253
                                    for i in arange(1,lg).reshape(-1):
                                        score[k][l][i]=dot(score[k][l](i),(1 + atan(dw / min(i,dw) - 1))) / (1 + atan(dw - 1))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:255
                        n=mirscalar(fl,'Data',score,'Title','Novelty')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:261
                else:
                    if logical_not(isa(orig,'mirscalar')):
                        s=get(orig,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:265
                        cl=get(orig,'Clusters')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:266
                        if isempty(cl):
                            dw=get(orig,'DiagWidth')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:268
                            Ks=option.K
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:269
                            for k in arange(1,length(s)).reshape(-1):
                                for i in arange(1,length(Ks)).reshape(-1):
                                    if isnumeric(dw):
                                        dwk=copy(dw)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:273
                                    else:
                                        dwk=dw[k]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:275
                                    if logical_not(isnan(Ks(i))) and Ks(i):
                                        cgs=min(Ks(i),dwk)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:278
                                    else:
                                        cgs=copy(dwk)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:280
                                    cg=checkergauss(cgs,option.transf) / cgs
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:282
                                    if strcmpi(postoption.direct,'Back'):
                                        cg[arange(),arange(cgs / 2 + 1,end())]=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:284
                                    else:
                                        if strcmpi(postoption.direct,'Forth'):
                                            cg[arange(),arange(1,cgs / 2)]=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:286
                                    #                 disp('Computing convolution, please wait...')
                                    for z in arange(1,length(s[k])).reshape(-1):
                                        sz=s[k][z]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:290
                                        szma=max(max(sz))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:291
                                        szmi=min(min(sz))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:292
                                        sz=(sz - szmi) / (szma - szmi)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:293
                                        sz=dot(2,sz) - 1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:294
                                        sz[isnan(sz)]=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:295
                                        cv=convolve2(sz,cg,'same')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:296
                                        nl=size(cv,1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:297
                                        nc=size(cv,2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:298
                                        if nl == 0:
                                            warning('WARNING IN NOVELTY: No frame decomposition. The novelty score cannot be computed.')
                                            score[k][z]=[]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:301
                                        else:
                                            sco=cv(floor(size(cv,1) / 2),arange())
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:303
                                            if postoption.filterborder:
                                                incr=find(diff(sco) >= 0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:305
                                                if not_(isempty(incr)):
                                                    decr=find(diff(sco) <= 0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:307
                                                    sco[arange(1,incr(1) - 1)]=NaN(1,incr(1) - 1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:308
                                                    if not_(isempty(decr)):
                                                        sco[arange(decr(end()) + 1,end())]=NaN(1,length(sco) - decr(end()))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:310
                                                    incr=find(diff(sco) >= 0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:312
                                                    sco2=copy(sco)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:313
                                                    if not_(isempty(incr)):
                                                        sco2=sco2(arange(1,incr(end()) + 1))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:315
                                                    decr=find(diff(sco) <= 0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:317
                                                    if not_(isempty(decr)) and decr(1) > 2:
                                                        sco2=sco2(arange(decr(1) - 1,end()))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:319
                                                    mins=min(sco2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:321
                                                    rang=find(sco >= mins)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:322
                                                    if not_(isempty(rang)):
                                                        sco[arange(1,rang(1) - 1)]=NaN(1,rang(1) - 1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:324
                                                        sco[arange(rang(end()) + 1,end())]=NaN(1,length(sco) - rang(end()))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:325
                                            score[k][z][i,arange()]=sco.T
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:329
                        else:
                            score=cell(1,length(s))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:335
                            for k in arange(1,length(s)).reshape(-1):
                                score[k]=cell(1,length(s[k]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:337
                                for z in arange(1,length(s[k])).reshape(-1):
                                    score[k][z]=zeros(1,size(cl[k][z],1))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:339
                                    for i in arange(1,length(cl[k][z])).reshape(-1):
                                        for j in arange(1,length(cl[k][z])).reshape(-1):
                                            clij=cl[k][z](i,j)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:342
                                            if logical_not(isnan(clij)):
                                                score[k][z][i]=max(score[k][z](i),dot(clij ** 5,j ** 2))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:344
                                                score[k][z][i + j]=max(score[k][z](i + j),dot(clij ** 5,j ** 2))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:346
                                    #fp{k}{z} = [fp{k}{z}(1,2:end);fp{k}{z}(2,1:end-1)];
                    else:
                        score=get(orig,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:356
    
    if not_(isempty(postoption)):
        if postoption.integr:
            for k in arange(1,length(score)).reshape(-1):
                for l in arange(1,length(score[k])).reshape(-1):
                    for i in arange(1,size(score[k][l],1)).reshape(-1):
                        sco=score[k][l](i,arange())
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:364
                        for j in arange(2,length(sco)).reshape(-1):
                            sco[j]=sco(j) + dot(sco(j - 1),postoption.integr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:366
                        score[k][l][i,arange()]=sco
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:368
        if postoption.filter:
            #a1 = exp(-1/(.1*4));
            a2=exp(- 1 / (dot(0.5,4)))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:375
            resp1=concat([[0.5],[0.8],[1]])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:377
            resp2=filter(1 - a2,concat([1,- a2]),concat([[ones(10,1)],[zeros(30,1)]]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:378
            resp=concat([[resp1],[resp2(arange(11,30))]])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:379
            for k in arange(1,length(score)).reshape(-1):
                for l in arange(1,length(score[k])).reshape(-1):
                    score[k][l]=conv(score[k][l],resp,'same')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:382
        if postoption.normal:
            for k in arange(1,length(score)).reshape(-1):
                for l in arange(1,length(score[k])).reshape(-1):
                    for i in arange(1,size(score[k][l],1)).reshape(-1):
                        sco=score[k][l](i,arange())
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:390
                        sco=(sco - min(sco)) / (max(sco) - min(sco))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:391
                        score[k][l][i,arange()]=sco
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:392
    
    n=mirscalar(orig,'Data',score,'Title','Novelty')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:399
    
    y=cellarray([n,orig])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:400
    
@function
def checkergauss(N=None,transf=None,*args,**kwargs):
    varargin = checkergauss.varargin
    nargin = checkergauss.nargin

    #hN = ceil(N/2);
    hN=(N - 1) / 2 + 1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:405
    if strcmpi(transf,'TimeLag') or strcmpi(transf,'Standard'):
        y=zeros(dot(2,N),N)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:407
        for j in arange(1,N).reshape(-1):
            for i in arange(1,dot(2,N) + 1).reshape(-1):
                g=exp(dot(- ((((i - N) - (j - hN)) / hN) ** 2 + (((j - hN) / hN) ** 2)),4))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:410
                if xor(j > hN,j - hN > i - N):
                    y[i,j]=- g
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:412
                else:
                    y[i,j]=g
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:414
    else:
        y=zeros(N)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:419
        for i in arange(1,N).reshape(-1):
            for j in arange(1,N).reshape(-1):
                g=exp(dot(- (((i - hN) / hN) ** 2 + (((j - hN) / hN) ** 2)),4))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:422
                if xor(j - hN > floor((i - hN) / 2),j - hN > floor((hN - i) / 2)):
                    y[i,j]=- g
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:424
                else:
                    y[i,j]=g
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirnovelty.m:426
    