﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on March 28, 2024, at 23:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'Musicrating'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 100):03.0f}",
    'session': '01',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\UserPC\\Desktop\\New folder\\code\\untitled.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1200,800], fullscr=False, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-0.2314, 0.1216, 0.8353], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.2314, 0.1216, 0.8353]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='ptb')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='PsychToolbox')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "trial" ---
    SessionWelcomeMsg = visual.TextStim(win=win, name='SessionWelcomeMsg',
        text='Music rating session\n\npress [space] to begin',
        font='consolas',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    KeyStartSession = keyboard.Keyboard()
    # Set experiment start values for variable component RepCount
    RepCount = 0
    RepCountContainer = []
    
    # --- Initialize components for Routine "music" ---
    ImageMegaphone = visual.ImageStim(
        win=win,
        name='ImageMegaphone', units='height', 
        image='megaphone.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    audiosample = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='audiosample')
    audiosample.setVolume(1.0)
    
    # --- Initialize components for Routine "rating" ---
    EmotionRating = visual.Slider(win=win, name='EmotionRating',
        startValue=0, size=(0.8, 0.03), pos=(0, -0.2), units='height',
        labels=('very\nsad','','','','','neutral','','','','','very\nhappy'), ticks=(-10,-8,-6,-4,-2,0,2,4,6,8,10), granularity=0.0,
        style='rating', styleTweaks=('labels45',), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor=[0.9216, 0.9216, 0.9216], lineColor=[0.7255, 0.7255, 0.7255], colorSpace='rgb',
        font='Consolas', labelHeight=0.019,
        flip=False, ori=0.0, depth=0, readOnly=False)
    TextRating = visual.TextStim(win=win, name='TextRating',
        text='Rate the piece emotion (-10 = very sad, 10 = very happy)\npress [space] when done rating',
        font='consolas',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-1.0);
    KeyConfirmRating = keyboard.Keyboard()
    
    # --- Initialize components for Routine "break_between" ---
    SmallBreakT = visual.TextStim(win=win, name='SmallBreakT',
        text='rating saved,' + str(RepCount) + ' from 4 samples done\npress [space] to listen to the next piece',
        font='consolas',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    continuepress = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ending" ---
    Ending = visual.TextStim(win=win, name='Ending',
        text='the experiment is complete\nthank you for your sacrifice\npress [space] to exit',
        font='consolas',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial.started', globalClock.getTime())
    KeyStartSession.keys = []
    KeyStartSession.rt = []
    _KeyStartSession_allKeys = []
    # keep track of which components have finished
    trialComponents = [SessionWelcomeMsg, KeyStartSession]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SessionWelcomeMsg* updates
        
        # if SessionWelcomeMsg is starting this frame...
        if SessionWelcomeMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SessionWelcomeMsg.frameNStart = frameN  # exact frame index
            SessionWelcomeMsg.tStart = t  # local t and not account for scr refresh
            SessionWelcomeMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SessionWelcomeMsg, 'tStartRefresh')  # time at next scr refresh
            # update status
            SessionWelcomeMsg.status = STARTED
            SessionWelcomeMsg.setAutoDraw(True)
        
        # if SessionWelcomeMsg is active this frame...
        if SessionWelcomeMsg.status == STARTED:
            # update params
            pass
        
        # *KeyStartSession* updates
        
        # if KeyStartSession is starting this frame...
        if KeyStartSession.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KeyStartSession.frameNStart = frameN  # exact frame index
            KeyStartSession.tStart = t  # local t and not account for scr refresh
            KeyStartSession.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyStartSession, 'tStartRefresh')  # time at next scr refresh
            # update status
            KeyStartSession.status = STARTED
            # keyboard checking is just starting
            KeyStartSession.clock.reset()  # now t=0
        if KeyStartSession.status == STARTED:
            theseKeys = KeyStartSession.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _KeyStartSession_allKeys.extend(theseKeys)
            if len(_KeyStartSession_allKeys):
                KeyStartSession.keys = _KeyStartSession_allKeys[-1].name  # just the last key pressed
                KeyStartSession.rt = _KeyStartSession_allKeys[-1].rt
                KeyStartSession.duration = _KeyStartSession_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial.stopped', globalClock.getTime())
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    musicRatingLoop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('audiosample.xlsx'),
        seed=None, name='musicRatingLoop')
    thisExp.addLoop(musicRatingLoop)  # add the loop to the experiment
    thisMusicRatingLoop = musicRatingLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMusicRatingLoop.rgb)
    if thisMusicRatingLoop != None:
        for paramName in thisMusicRatingLoop:
            globals()[paramName] = thisMusicRatingLoop[paramName]
    
    for thisMusicRatingLoop in musicRatingLoop:
        currentLoop = musicRatingLoop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisMusicRatingLoop.rgb)
        if thisMusicRatingLoop != None:
            for paramName in thisMusicRatingLoop:
                globals()[paramName] = thisMusicRatingLoop[paramName]
        
        # --- Prepare to start Routine "music" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music.started', globalClock.getTime())
        audiosample.setSound(AudioSample, secs=4, hamming=True)
        audiosample.setVolume(1.0, log=False)
        audiosample.seek(0)
        # keep track of which components have finished
        musicComponents = [ImageMegaphone, audiosample]
        for thisComponent in musicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "music" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ImageMegaphone* updates
            
            # if ImageMegaphone is starting this frame...
            if ImageMegaphone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ImageMegaphone.frameNStart = frameN  # exact frame index
                ImageMegaphone.tStart = t  # local t and not account for scr refresh
                ImageMegaphone.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ImageMegaphone, 'tStartRefresh')  # time at next scr refresh
                # update status
                ImageMegaphone.status = STARTED
                ImageMegaphone.setAutoDraw(True)
            
            # if ImageMegaphone is active this frame...
            if ImageMegaphone.status == STARTED:
                # update params
                pass
            
            # if ImageMegaphone is stopping this frame...
            if ImageMegaphone.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ImageMegaphone.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    ImageMegaphone.tStop = t  # not accounting for scr refresh
                    ImageMegaphone.frameNStop = frameN  # exact frame index
                    # update status
                    ImageMegaphone.status = FINISHED
                    ImageMegaphone.setAutoDraw(False)
            
            # if audiosample is starting this frame...
            if audiosample.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                audiosample.frameNStart = frameN  # exact frame index
                audiosample.tStart = t  # local t and not account for scr refresh
                audiosample.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                audiosample.status = STARTED
                audiosample.play()  # start the sound (it finishes automatically)
            
            # if audiosample is stopping this frame...
            if audiosample.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > audiosample.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    audiosample.tStop = t  # not accounting for scr refresh
                    audiosample.frameNStop = frameN  # exact frame index
                    # update status
                    audiosample.status = FINISHED
                    audiosample.stop()
            # update audiosample status according to whether it's playing
            if audiosample.isPlaying:
                audiosample.status = STARTED
            elif audiosample.isFinished:
                audiosample.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in musicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music" ---
        for thisComponent in musicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music.stopped', globalClock.getTime())
        audiosample.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "rating" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('rating.started', globalClock.getTime())
        EmotionRating.reset()
        KeyConfirmRating.keys = []
        KeyConfirmRating.rt = []
        _KeyConfirmRating_allKeys = []
        # keep track of which components have finished
        ratingComponents = [EmotionRating, TextRating, KeyConfirmRating]
        for thisComponent in ratingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "rating" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EmotionRating* updates
            
            # if EmotionRating is starting this frame...
            if EmotionRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EmotionRating.frameNStart = frameN  # exact frame index
                EmotionRating.tStart = t  # local t and not account for scr refresh
                EmotionRating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EmotionRating, 'tStartRefresh')  # time at next scr refresh
                # update status
                EmotionRating.status = STARTED
                EmotionRating.setAutoDraw(True)
            
            # if EmotionRating is active this frame...
            if EmotionRating.status == STARTED:
                # update params
                pass
            
            # *TextRating* updates
            
            # if TextRating is starting this frame...
            if TextRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TextRating.frameNStart = frameN  # exact frame index
                TextRating.tStart = t  # local t and not account for scr refresh
                TextRating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TextRating, 'tStartRefresh')  # time at next scr refresh
                # update status
                TextRating.status = STARTED
                TextRating.setAutoDraw(True)
            
            # if TextRating is active this frame...
            if TextRating.status == STARTED:
                # update params
                pass
            
            # *KeyConfirmRating* updates
            
            # if KeyConfirmRating is starting this frame...
            if KeyConfirmRating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                KeyConfirmRating.frameNStart = frameN  # exact frame index
                KeyConfirmRating.tStart = t  # local t and not account for scr refresh
                KeyConfirmRating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeyConfirmRating, 'tStartRefresh')  # time at next scr refresh
                # update status
                KeyConfirmRating.status = STARTED
                # keyboard checking is just starting
                KeyConfirmRating.clock.reset()  # now t=0
                KeyConfirmRating.clearEvents(eventType='keyboard')
            if KeyConfirmRating.status == STARTED:
                theseKeys = KeyConfirmRating.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _KeyConfirmRating_allKeys.extend(theseKeys)
                if len(_KeyConfirmRating_allKeys):
                    KeyConfirmRating.keys = _KeyConfirmRating_allKeys[-1].name  # just the last key pressed
                    KeyConfirmRating.rt = _KeyConfirmRating_allKeys[-1].rt
                    KeyConfirmRating.duration = _KeyConfirmRating_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ratingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rating" ---
        for thisComponent in ratingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('rating.stopped', globalClock.getTime())
        musicRatingLoop.addData('EmotionRating.response', EmotionRating.getRating())
        musicRatingLoop.addData('EmotionRating.rt', EmotionRating.getRT())
        # check responses
        if KeyConfirmRating.keys in ['', [], None]:  # No response was made
            KeyConfirmRating.keys = None
        musicRatingLoop.addData('KeyConfirmRating.keys',KeyConfirmRating.keys)
        if KeyConfirmRating.keys != None:  # we had a response
            musicRatingLoop.addData('KeyConfirmRating.rt', KeyConfirmRating.rt)
            musicRatingLoop.addData('KeyConfirmRating.duration', KeyConfirmRating.duration)
        # the Routine "rating" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "break_between" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('break_between.started', globalClock.getTime())
        continuepress.keys = []
        continuepress.rt = []
        _continuepress_allKeys = []
        # keep track of which components have finished
        break_betweenComponents = [SmallBreakT, continuepress]
        for thisComponent in break_betweenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "break_between" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SmallBreakT* updates
            
            # if SmallBreakT is starting this frame...
            if SmallBreakT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallBreakT.frameNStart = frameN  # exact frame index
                SmallBreakT.tStart = t  # local t and not account for scr refresh
                SmallBreakT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallBreakT, 'tStartRefresh')  # time at next scr refresh
                # update status
                SmallBreakT.status = STARTED
                SmallBreakT.setAutoDraw(True)
            
            # if SmallBreakT is active this frame...
            if SmallBreakT.status == STARTED:
                # update params
                pass
            
            # *continuepress* updates
            
            # if continuepress is starting this frame...
            if continuepress.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continuepress.frameNStart = frameN  # exact frame index
                continuepress.tStart = t  # local t and not account for scr refresh
                continuepress.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continuepress, 'tStartRefresh')  # time at next scr refresh
                # update status
                continuepress.status = STARTED
                # keyboard checking is just starting
                continuepress.clock.reset()  # now t=0
                continuepress.clearEvents(eventType='keyboard')
            if continuepress.status == STARTED:
                theseKeys = continuepress.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _continuepress_allKeys.extend(theseKeys)
                if len(_continuepress_allKeys):
                    continuepress.keys = _continuepress_allKeys[-1].name  # just the last key pressed
                    continuepress.rt = _continuepress_allKeys[-1].rt
                    continuepress.duration = _continuepress_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_betweenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_between" ---
        for thisComponent in break_betweenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('break_between.stopped', globalClock.getTime())
        # the Routine "break_between" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'musicRatingLoop'
    
    
    # --- Prepare to start Routine "ending" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ending.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    endingComponents = [Ending, key_resp]
    for thisComponent in endingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ending" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Ending* updates
        
        # if Ending is starting this frame...
        if Ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ending.frameNStart = frameN  # exact frame index
            Ending.tStart = t  # local t and not account for scr refresh
            Ending.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ending, 'tStartRefresh')  # time at next scr refresh
            # update status
            Ending.status = STARTED
            Ending.setAutoDraw(True)
        
        # if Ending is active this frame...
        if Ending.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ending" ---
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ending.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "ending" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
