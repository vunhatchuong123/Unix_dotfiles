local options = {
  clipboard = "unnamedplus", -- allows neovim to access the system clipboard
  hidden = true, -- required to keep multiple buffers and open multiple buffers
  -- guicursor = "",
  completeopt = { "menuone", "noselect" }, -- mostly just for cmp
  hlsearch = false, -- Default | highlight all matches on previous search pattern
  incsearch = true, -- Makes search act like search in modern browsers
  splitbelow = true, -- force all horizontal splits to go below current window
  splitright = true, -- force all vertical splits to go to the right of current window

  ignorecase = true, -- ignore case in search patterns
  smartcase = true, -- unless there is a capital letter in the query
  inccommand = "split",

  -- SYSTEM --
  -- shell = "powershell.exe",
  updatetime = 50, -- faster completion (4000ms default)
  swapfile = false, -- Don't create a swapfile
  backup = false, -- Default | creates a backup file
  writebackup = false, -- if a file is being edited by another program (or was written to file while editing with another program), it is not allowed to be edited
  undofile = true, -- enable persistent undo
 -- guifont = "JetBrains Mono",



  -- APPEARANCE --
  termguicolors = true, -- set term gui colors (most terminals support this)
  signcolumn = "yes", -- always show the sign column, otherwise it would shift the text each time
  colorcolumn = "80",
  cmdheight = 1, -- more space in the neovim command line for displaying messages
  showtabline = 0, -- always show tabs
  scrolloff = 8, -- minimal number of screen lines to keep above and below the cursor.
  sidescrolloff = 8, -- minimal number of screen lines to keep left and right of the cursor.Only available with wrap off
  number = true, -- set numbered lines
  relativenumber = true, -- set relative numbered lines
  showmode = false,
  -- showcmd = false, -- Show what you type


  -- INDENT --
  breakindent = true,
  linebreak = true,
  breakindentopt = sbr,
  showbreak = "↪>\\",
  --showbreak = string.rep(" ", 3) -- Make it so that long lines wrap smartly

  --TABS --
  wrap = false,
  smartindent = true, -- make indenting smarter again
  expandtab = true, -- convert tabs to spaces
  softtabstop = 2,
  shiftwidth = 2, -- the number of spaces inserted for each indentation
  tabstop = 2, -- insert 4 spaces for a tab
  --foldmethod = "expr",
  --foldexpr = "nvim_treesitter#foldexpr()",
  foldlevelstart = 99,

}

---  SETTINGS  ---
vim.opt.shortmess:append "c" -- don't show redundant messages from ins-completion-menu
vim.opt.fillchars = vim.opt.fillchars + 'eob: '
vim.opt.fillchars:append {
  -- foldopen = "",
  -- foldclose = "",
  stl = ' ',
}
-- vim.g.loaded_netrw = 1 -- Disable netrw
-- vim.g.loaded_netrwPlugin = 1

-- EXECUTE --
for k, v in pairs(options) do
  vim.opt[k] = v
end

vim.cmd "set whichwrap+=<,>,[,],h,l"
vim.cmd [[set iskeyword+=-]]

-- Need to disable first for treesitter installation
