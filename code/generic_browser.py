from talon import Module, Context

mod = Module()
ctx = Context()
mod.list('browser_shortcut', desc='Website shortcuts')
# Maybe use a capture so the capitals don't mess up?
ctx.lists['self.browser_shortcut'] = {
    'Amazon': 'https://www.amazon.com/',
    'canvas': 'https://canvas.rutgers.edu/',
    'male': 'https://gmail.com/',
    'mail': 'https://gmail.com/',
    'Scarlet male': 'https://mail.google.com/mail/u/1/#inbox',
    'Scarlet mail': 'https://mail.google.com/mail/u/1/#inbox',
    'Drive': 'https://drive.google.com/drive/my-drive',
    'Scarlet Drive': 'https://drive.google.com/drive/u/1/my-drive',
    'YouTube': 'https://www.youtube.com/',
    'get hub': 'https://github.com/',
    'Reddit': 'https://www.reddit.com/',
    'physics': 'https://general.physics.rutgers.edu/online/204/index.shtml',
    'physics textbook': 'chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/file:///C:/Users/Sean/Desktop/Physics/John%20D.%20Cutnell,%20Kenneth%20W.%20Johnson,%20David%20Young,%20Shane%20Stadler%20-%20Physics-Wiley%20(2018).pdf',
    'physics formulas': 'chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/file:///C:/Users/Sean/Desktop/Physics/formula204.pdf',
    'symbol lab': 'http://symbolab.com/',
    'talents lack': 'https://app.slack.com/client/T7FPSMV8F',
    'Talon practice': 'https://chaosparrot.github.io/talon_practice/',
    'Talon docs': 'https://talonvoice.com/docs/',
    'Talon wiki': "https://talon.wiki/",
    'repository': 'https://github.com/SeanTaylorLane/knausj_talon',
    'community repository': 'https://github.com/knausj85/knausj_talon',
}
