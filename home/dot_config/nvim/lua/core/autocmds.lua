
local augroup = vim.api.nvim_create_augroup
general_setting = augroup('general_setting', {})

local autocmd = vim.api.nvim_create_autocmd
local yank_group = augroup('HighlightYank', {})


autocmd( "TextYankPost" , {
  group = yank_group,
  pattern = "*",
  callback = function()
    vim.highlight.on_yank { higroup = "IncSearch", timeout = 40 
    }
  end,
})

autocmd( "BufWinEnter" , {
  group = general_setting,
  pattern = "*",
  callback = function()
    vim.cmd "set formatoptions-=cro"
  end,
})

autocmd( "VimResized", {
  group = general_setting,
  callback = function()
    vim.cmd "tabdo wincmd ="
  end,
})
autocmd( {"BufWinEnter","FileReadPost"} , {
  group = general_setting,
  pattern = "*",
  callback = function()
    vim.cmd "normal zR"
    end,
})


